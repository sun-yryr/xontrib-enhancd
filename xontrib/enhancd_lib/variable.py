import xonsh.built_ins as built_ins
from pathlib import Path
from . import x_env

__keys = x_env.keys()

# ENHANCD_ROOT
# ENHANCD_COMMAND
ENHANCD_FILTER = x_env["ENHANCD_FILTER"] if "ENHANCD_FILTER" in __keys else "peco:fzf"
ENHANCD_DIR = Path(x_env["ENHANCD_DIR"]).resolve() if "ENHANCD_DIR" in __keys else Path(x_env["HOME"] + "/.enhancd")
ENHANCD_DISABLE_DOT = x_env["ENHANCD_DISABLE_DOT"] if "ENHANCD_DISABLE_DOT" in __keys else "0"
ENHANCD_DISABLE_HYPHEN = x_env["ENHANCD_DISABLE_HYPHEN"] if "ENHANCD_DISABLE_HYPHEN" in __keys else "0"
ENHANCD_DISABLE_HOME = x_env["ENHANCD_DISABLE_HOME"] if "ENHANCD_DISABLE_HOME" in __keys else "0"
ENHANCD_DOT_ARG = x_env["ENHANCD_DOT_ARG"] if "ENHANCD_DOT_ARG" in __keys else ".."
ENHANCD_HYPHEN_ARG = x_env["ENHANCD_HYPHEN_ARG"] if "ENHANCD_HYPHEN_ARG" in __keys else "-"
ENHANCD_HYPHEN_NUM = x_env["ENHANCD_HYPHEN_NUM"] if "ENHANCD_HYPHEN_NUM" in __keys else "10"
ENHANCD_HOME_ARG = x_env["ENHANCD_HOME_ARG"] if "ENHANCD_HOME_ARG" in __keys else ""
ENHANCD_USE_FUZZY_MATCH = x_env["ENHANCD_USE_FUZZY_MATCH"] if "ENHANCD_USE_FUZZY_MATCH" in __keys else "1"
# ENHANCD_COMPLETION_DEFAULT
ENHANCD_COMPLETION_KEYBIND = x_env["ENHANCD_COMPLETION_KEYBIND"] if "ENHANCD_COMPLETION_KEYBIND" in __keys else "^I"
ENHANCD_COMPLETION_BEHAVIOR = x_env["ENHANCD_COMPLETION_BEHAVIOR"] if "ENHANCD_COMPLETION_BEHAVIOR" in __keys else "default"

ENHANCD_HOOK_AFTER_CD = x_env["ENHANCD_HOOK_AFTER_CD"] if "ENHANCD_HOOK_AFTER_CD" in __keys else None

DEFAULT_CD = built_ins.builtins.aliases['cd']
OLDPWD = x_env["HOME"]

def reload_variables():
    """[環境変数の再読み込み]
    """    
    ENHANCD_FILTER = x_env["ENHANCD_FILTER"] if "ENHANCD_FILTER" in __keys else "peco:fzf"
    ENHANCD_DIR = Path(x_env["ENHANCD_DIR"]).resolve() if "ENHANCD_DIR" in __keys else Path(x_env["HOME"] + "/.enhancd")
    ENHANCD_DISABLE_DOT = x_env["ENHANCD_DISABLE_DOT"] if "ENHANCD_DISABLE_DOT" in __keys else "0"
    ENHANCD_DISABLE_HYPHEN = x_env["ENHANCD_DISABLE_HYPHEN"] if "ENHANCD_DISABLE_HYPHEN" in __keys else "0"
    ENHANCD_DISABLE_HOME = x_env["ENHANCD_DISABLE_HOME"] if "ENHANCD_DISABLE_HOME" in __keys else "0"
    ENHANCD_DOT_ARG = x_env["ENHANCD_DOT_ARG"] if "ENHANCD_DOT_ARG" in __keys else ".."
    ENHANCD_HYPHEN_ARG = x_env["ENHANCD_DOT_ARG"] if "ENHANCD_DOT_ARG" in __keys else "-"
    ENHANCD_HYPHEN_NUM = x_env["ENHANCD_HYPHEN_NUM"] if "ENHANCD_HYPHEN_NUM" in __keys else "10"
    ENHANCD_HOME_ARG = x_env["ENHANCD_HOME_ARG"] if "ENHANCD_HOME_ARG" in __keys else ""
    ENHANCD_USE_FUZZY_MATCH = x_env["ENHANCD_USE_FUZZY_MATCH"] if "ENHANCD_USE_FUZZY_MATCH" in __keys else "1"
    ENHANCD_COMPLETION_KEYBIND = x_env["ENHANCD_COMPLETION_KEYBIND"] if "ENHANCD_COMPLETION_KEYBIND" in __keys else "^I"
    ENHANCD_COMPLETION_BEHAVIOR = x_env["ENHANCD_COMPLETION_BEHAVIOR"] if "ENHANCD_COMPLETION_BEHAVIOR" in __keys else "default"
    ENHANCD_HOOK_AFTER_CD = x_env["ENHANCD_HOOK_AFTER_CD"] if "ENHANCD_HOOK_AFTER_CD" in __keys else None