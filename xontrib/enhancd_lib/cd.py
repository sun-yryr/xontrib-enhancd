from . import sources, history, filter as fil, filepath, x_env
from .variable import *
import argparse
from pathlib import Path

def before_cd():
    # OLDPWD の更新
    global OLDPWD
    OLDPWD = str(Path().resolve())

def after_cd():
    history.update_history()
    if ENHANCD_HOOK_AFTER_CD is not None:
        ENHANCD_HOOK_AFTER_CD()

def builtin_cd(args):
    before_cd()
    DEFAULT_CD([args])
    after_cd()


def __main(args, stdin=None, stdout=None, stderr=None, spec=None):
    if not sources.is_available():
        print("enhancd is not available")
        builtin_cd(args)
        return
    args = __parser(args)
    
    historyList = []
    if args.path == []:
        historyList.extend(history.get_history_list())
    for arg in args.path:
        if len(historyList) == 0:
            if arg == ENHANCD_HYPHEN_ARG:
                # add prev historyList 10count
                historyList = history.get_latest_history()
                continue
            elif arg == ENHANCD_DOT_ARG:
                # add parents
                historyList = filepath.list_parents()
                continue
            elif Path(arg).exists():
                historyList = [arg]
                break
            else:
                # add logs historyList
                historyList.extend(history.get_history_list())
        # fuzzy search
        historyList = fil.f_search(arg, historyList)
    if len(historyList) == 0:
        # error
        print("error")
    elif len(historyList) == 1:
        # builtin_cd
        builtin_cd(historyList[0])
    else:
        # filter tool
        builtin_cd(fil.interactive(historyList))
    
def __parser(args):
    parser = argparse.ArgumentParser(
        usage="cd [-h] [path [path ...]]" ,
        description="description"
    )
    parser.add_argument("path", nargs="*")
    return parser.parse_args(args)
