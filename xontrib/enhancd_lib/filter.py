from fuzzysearch import find_near_matches
from . import x_execer
from .variable import *
import subprocess

def f_search(keyword: str, paths: [str]):
    res = []
    for p in paths:
        if find_near_matches(keyword, p, max_l_dist=0) != []:
            # ヒット
            res.append(p)
    return res

def interactive(l: [str]):
    if len(l) <= 0:
        return None
    str_list = repr("\n".join(l))
    tmpFile = ENHANCD_DIR / "tmp"
    x_execer.eval(f'echo {str_list} | peco > {str(tmpFile)}')
    file = open(tmpFile, "r")
    select = str(file.read())
    file.close()
    tmpFile.unlink()
    if select is None:
        return None
    return select.rstrip("\n")