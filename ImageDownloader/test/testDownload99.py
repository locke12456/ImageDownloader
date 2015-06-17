import unittest
from modules.Comic99 import Comic99
from modules.Download99 import Download99

class Test_testDownload99(unittest.TestCase):
    def test_testDownload99(self):
        c99 = Download99("http://www.99comic.com/comic/9919814/")
        comic = c99.List()[0]
        comic.Download("./")
        #c99.Download("./")

if __name__ == '__main__':
    unittest.main()
