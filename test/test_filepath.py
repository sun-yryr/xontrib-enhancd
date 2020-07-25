import unittest
from unittest.mock import patch
from .mock_data import mock_xonsh, mock_aliases


class TestFilePath(unittest.TestCase):
    def setUp(self):
        self.patcher_xonsh = patch('builtins.__xonsh__', new=mock_xonsh, create=True)
        self.patcher_aliases = patch('builtins.aliases', new=mock_aliases, create=True)
        self.mock_xonsh = self.patcher_xonsh.start()
        self.mock_aliases = self.patcher_aliases.start()
    
    def tearDown(self):
        self.patcher_xonsh.stop()
        self.patcher_aliases.stop()
    
    @patch('xontrib.enhancd_lib.filepath.run')
    def test_split_filterlist(self, mock):
        from xontrib.enhancd_lib.filepath import split_filterlist
        i = 'peco:fzf:c'
        o = split_filterlist(i)
        self.assertIsNone(o)
        self.assertEqual(len(i.split(':')), mock.call_count)

    def test_list_parents(self):
        from xontrib.enhancd_lib.filepath import list_parents
        res = list_parents()
        self.assertIsInstance(res, list)
    
    def test_list_children(self):
        from xontrib.enhancd_lib.filepath import list_children
        res = list_children()
        self.assertIsInstance(res, list)
        


if __name__ == "__main__":
    unittest.main()
