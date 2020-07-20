import xonsh
from pathlib import Path
import xonsh.built_ins as built_ins
from .enhancd_lib.cd import __main
from .enhancd_lib import x_aliases, x_execer, x_env

__all__ = ()
# create Environment variables
__keys = x_env.keys()

# ENHANCD_ROOT
# ENHANCD_COMMAND
x_env["ENHANCD_FILTER"] = x_env.get("ENHANCD_FILTER", "peco:fzf")
x_env["ENHANCD_DIR"] = Path(x_env["ENHANCD_DIR"]).resolve() if "ENHANCD_DIR" in __keys else Path(x_env["HOME"] + "/.enhancd")
x_env["ENHANCD_DISABLE_DOT"] = x_env.get("ENHANCD_DISABLE_DOT", "0")
x_env["ENHANCD_DISABLE_HYPHEN"] = x_env.get("ENHANCD_DISABLE_HYPHEN", "0")
x_env["ENHANCD_DISABLE_HOME"] = x_env.get("ENHANCD_DISABLE_HOME", "0")
x_env["ENHANCD_DOT_ARG"] = x_env.get("ENHANCD_DOT_ARG", "..")
x_env["ENHANCD_HYPHEN_ARG"] = x_env.get("ENHANCD_HYPHEN_ARG", "-")
x_env["ENHANCD_HYPHEN_NUM"] = x_env.get("ENHANCD_HYPHEN_NUM", "10")
x_env["ENHANCD_HOME_ARG"] = x_env.get("ENHANCD_HOME_ARG", "")
x_env["ENHANCD_USE_FUZZY_MATCH"] = x_env.get("ENHANCD_USE_FUZZY_MATCH", "1")
# ENHANCD_COMPLETION_DEFAULT
x_env["ENHANCD_COMPLETION_KEYBIND"] = x_env.get("ENHANCD_COMPLETION_KEYBIND", "^I")
x_env["ENHANCD_COMPLETION_BEHAVIOR"] = x_env.get("ENHANCD_COMPLETION_BEHAVIOR", "default")
x_env["DEFAULT_CD"] = built_ins.builtins.aliases['cd']
x_env["ENHANCD_OLDPWD"] = x_env["HOME"]

def init():
    # create .enhancd dir & log file
    x_execer.eval(f'mkdir -p {str(x_env["ENHANCD_DIR"])}')
    x_execer.eval(f'touch {str(x_env["ENHANCD_DIR"] / "enhancd.log")}')

init()
x_aliases["cd"] = __main
