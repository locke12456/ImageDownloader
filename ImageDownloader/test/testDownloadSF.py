import unittest
from modules.DownloadSF import DownloadSF
class Test_testDownloadSF(unittest.TestCase):
    def test_Download(self):
        sf = DownloadSF("http://comic.sfacg.com/HTML/HSWYC/") 
        Comic = sf.List()[0]
        completed = Comic.Download("./")
        self.assertEqual(completed , True)
        
        #self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()
