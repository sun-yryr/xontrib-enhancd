import unittest
from unittest.mock import patch
from .mock_data import mock_xonsh, mock_aliases


class TestFilePath(unittest.TestCase):
    @patch('builtins.aliases', new=mock_aliases, create=True)
    @patch('builtins.__xonsh__', new=mock_xonsh, create=True)
    def test_split_filterlist(self):
        from xontrib.enhancd_lib import filepath
        i = 'peco:fzf:c'
        o = filepath.split_filterlist(i)
        self.assertTrue(o)

if __name__ == "__main__":
    unittest.main()
