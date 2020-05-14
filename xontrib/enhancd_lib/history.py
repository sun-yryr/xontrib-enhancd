from .variable import *
from . import filepath, filter as fil, x_env

def open_history():
    logpath = ENHANCD_DIR / "enhancd.log"
    with open(logpath, "r") as f:
        return f.read().rstrip("\n").split("\n")

def update_history():
    history = filepath.list_parents(reverse=True)
    history.extend(filepath.list_children())
    history.extend(open_history())
    history.append(str(Path().resolve()))

    history.reverse()
    newHistory = list(dict.fromkeys(history))
    newHistory.reverse()
    if len(newHistory) > 0:
        newHistory = list(filter(lambda a: a != '', newHistory))
        logpath = ENHANCD_DIR / "enhancd.log"
        with open(logpath, "w") as f:
            return f.write("\n".join(newHistory))

def get_history_list(keyword=None):
    history = open_history()
    history.reverse()
    history = list(dict.fromkeys(history))
    history = exists(history)
    if keyword is not None:
        history = fil.f_search(keyword, paths=history)
    PWD = str(Path().resolve())
    if PWD in history:
        history.remove(PWD)
    return history

def get_latest_history(keyword: str=None):
    if ENHANCD_DISABLE_HYPHEN == 1:
        return OLDPWD
    l = get_history_list()
    if x_env["HOME"] in l:
        l.remove(x_env["HOME"])
    l = l[:int(ENHANCD_HYPHEN_NUM)]
    return l

def unique(history: [str]):
    res = []
    for i in history:
        if not i in res:
            res.append(i)
    return res


def exists(paths: [str]):
    """[存在するパスのみを抽出して返却する]

    Args:
        paths ([str]): [パスの配列（enhancd.logと同じ）]

    Returns:
        [str]: [存在するパスの配列]
    """    
    return list(filter(lambda p: Path(p).exists(), paths))
