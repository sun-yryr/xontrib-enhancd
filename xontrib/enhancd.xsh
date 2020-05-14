import xonsh
from .src.cd import __main
from .src.variable import reload_variables

__all__ = ()

aliases["cd"] = __main
aliases["enhancd_reload"] = reload_variables
