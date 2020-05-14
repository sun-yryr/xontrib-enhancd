import xonsh
from .enhancd_lib.cd import __main
from .enhancd_lib.variable import reload_variables, ENHANCD_DIR
from .enhancd_lib import x_aliases, x_execer

__all__ = ()

def init():
    # create .enhancd dir & log file
    x_execer.eval(f'mkdir -p {str(ENHANCD_DIR)}')
    x_execer.eval(f'touch {str(ENHANCD_DIR / "enhancd.log")}')

init()
x_aliases["cd"] = __main
x_aliases["enhancd_reload"] = reload_variables
