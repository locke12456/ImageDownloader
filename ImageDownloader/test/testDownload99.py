import unittest
from plugins.Comic99 import Comic99
from plugins.Download99 import Download99

class Test_testDownload99(unittest.TestCase):
    def test_testDownload99(self):
        c99 = Download99("http://www.99comic.com/comic/991234/")
        for i in range(len(c99.List())-3,len(c99.List())):
            comic = c99.List()[i]
            comic.Download("./")
        #c99.Download("./")

if __name__ == '__main__':
    unittest.main()
