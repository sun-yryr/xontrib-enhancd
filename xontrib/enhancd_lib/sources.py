from . import filepath
from .variable import *
from pathlib import Path

def is_available():
    """[filterツールとenhancd.logが存在することを確認する]

    Returns:
        [bool]: [実行可能ならTrue]
    """    
    b1 = filepath.split_filterlist(ENHANCD_FILTER)
    b2 = (ENHANCD_DIR / "enhancd.log").exists()
    return b1 and b2
