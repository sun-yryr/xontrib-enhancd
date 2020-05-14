import unittest
from xontrib.enhancd_lib import filepath

class TestFilePath(unittest.TestCase): 
    def test_split_filterlist(self):
        i = 'peco:fzf:c'
        o = filepath.split_filterlist(i)
        self.assertTrue(o)

if __name__ == "__main__":
    unittest.main()
