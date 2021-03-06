from DownloadBase import DownloadBase
from ComicBase import ComicBase , urllib
from plugins.ComicSF import ComicSF
import re
from html2text import html2text
class DownloadSF(DownloadBase):
    """description of class"""
    __search_all__ ="(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))"
    __host_patterns__ = __search_all__+"+/"
    __sect_patterns__ = __search_all__+"+/"
    __comic_name_patterns__ = "mh.sfacg.com/Logo"
    __url__ = "comic.sfacg.com/"

    __book_list__ = []
    __url_list__ = []
    
    __class_name__ = "DownloadSF"

    @classmethod
    def __register__(self , classname):
        return classname == self.__class_name__

    def __init__(self, url, *args, **kwargs):
        super(DownloadSF, self).__init__(url, *args, **kwargs)
        self.__parse__(url)

    def _build_comices(self, base, list, url):
        for tag in list:
            sect = tag[1].split(base)
            temp = sect[1].split("/")
            tempurl = url+sect[1]
            self.__url_list__.append(tempurl)
            sf = ComicSF(tempurl , temp[0])
            sf.Tag = tag[0]
            self.__book_list__.append(sf)

    def _get_name(self, html):
        for name in self.__get_comic_name__(html):
            self.Name = name[0]

    def __build_book_list__(self, base, html, url):
        #list = re.findall(base + self.__host_patterns__ , html)
        list = self.__export_book_to_dict__(base, html)
        self._get_name(html)
        self._build_comices(base, list, url)
        self.__book_list__ = sorted(self.__book_list__, key=lambda k: k.Name) 
    def __parse__( self , url ):
        compare_url = url.split( self.__url__ )
        if len( compare_url ) is not 2 :
            return False
        self.URL = url
        base = compare_url[1]
        #self.__comic_name_patterns__ = base + self.__comic_name_patterns__
        page = urllib.urlopen(url)
        html = page.read().decode('utf-8')
        page.close()
        self.__build_book_list__(base, html, url)
        return True
    def List(self):
        return self.__book_list__

