from DownloadBase import DownloadBase
from ComicBase import ComicBase , urllib
import re
from modules.Comic99 import Comic99
from html2text import html2text
class Download99(DownloadBase):
    """description of class"""
    __search_all__ ="(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))"
    __host_patterns__ = "comics/"+__search_all__+"+/"
    __comic_name_patterns__ = __search_all__+"+/"
    __name_patterns__ = '(?:[0-9])'
    __sect_patterns__ = __search_all__+"+/"
    __url__ = "www.99comic.com/"

    __book_list__ = []
    __url_list__ = []

    def __init__(self, url, *args, **kwargs):
        super(Download99, self).__init__(url, *args, **kwargs)
        self.__parse__(url)

    def _build_comices(self, list):
        for tag in list:
            temp = "http://"+self.__url__+tag[1]
            self.__url_list__.append(temp)
            try:
                name = re.findall(self.__name_patterns__ , tag[0])
            except Exception:
                continue
            num = ""
            for _ in name:
                num += _
            c99 = Comic99( temp , num)
            c99.Tag = tag[0]
            self.__book_list__.append(c99)
        return name

    def _get_name(self, html):
        comic_name_list = self.__get_comic_name__( html)
        for name in comic_name_list:
            temp = name[0]
            if len(temp.split("Rss")) < 2 :
                self.Name = temp

    def __build_book_list__(self, base, html, url):
        list = self.__export_book_to_dict__(base, html)
        self._get_name(html) 
        name = self._build_comices(list)
        self.__book_list__ = sorted(self.__book_list__, key=lambda k: k.Name) 
    def __parse__( self , url ):
        compare_url = url.split( self.__url__ )
        if len( compare_url ) is not 2 :
            return False
        self.URL = url
        base = "comics/"
        self.__comic_name_patterns__ = compare_url[1]
        page = urllib.urlopen(url)
        html = page.read().decode("utf-8")
        page.close()
        self.__build_book_list__(base, html, url)
        return True
    def List(self):
        return self.__book_list__

