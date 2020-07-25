from unittest.mock import patch, MagicMock

__xonsh__ = {
    "env": {

    },
    "execer": MagicMock()
}
mock_xonsh = MagicMock()
mock_xonsh.__getitem__.side_effect = __xonsh__.__getitem__
mock_aliases = MagicMock()