import unittest
from plugins.DownloadSF import DownloadSF
class Test_testDownloadSF(unittest.TestCase):
    def test_List(self):
        sf = DownloadSF("http://comic.sfacg.com/HTML/HSWYC/") 
        ComicList = sf.List()
        for comic in ComicList:
            print comic.Name + " : " + comic.URL

    def test_Download(self):
        
        sf = DownloadSF("http://comic.sfacg.com/HTML/xinsjfyzs/") 
        Comic = sf.List()[5]
        completed = Comic.Download("./")
        self.assertEqual(completed , True)
        
        #self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()
