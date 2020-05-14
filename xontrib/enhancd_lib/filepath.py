from subprocess import run, DEVNULL
from pathlib import Path

def split_filterlist(s: str):
    """[return True if filterCommand exists]

    Args:
        s (str): [FilterCommands ex: peco:fzf]

    Returns:
        [bool]
    """    
    if not s:
        exit(1)
    for filterCmd in s.split(":"):
        pc = run(['which', filterCmd], stdout=DEVNULL)
        if pc.returncode == 0:
            return True
    return False

def list_parents(reverse=False):
    p = Path().resolve()
    res = list(map(str, p.parents))
    if reverse:
        return list(reversed(res))
    return res

def list_children():
    p = Path().resolve()
    return [str(a) for a in p.iterdir() if a.is_dir() and a.name[0]!="."]
