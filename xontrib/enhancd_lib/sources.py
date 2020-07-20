from . import filepath, x_env

def is_available():
    """[filterツールとenhancd.logが存在することを確認する]

    Returns:
        [bool]: [実行可能ならTrue]
    """    
    b1 = filepath.split_filterlist(x_env["ENHANCD_FILTER"]) is not None
    b2 = (x_env["ENHANCD_DIR"] / "enhancd.log").exists()
    return b1 and b2
