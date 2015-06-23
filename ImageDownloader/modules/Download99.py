from DownloadBase import DownloadBase
from ComicBase import ComicBase , urllib
import re
from modules.Comic99 import Comic99
from html2text import html2text
class Download99(DownloadBase):
    """description of class"""
    __search_all__ ="(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))"
    __host_patterns__ = "comics/"+__search_all__+"+/"
    __name_patterns__ = '(?:[0-9])'
    __sect_patterns__ = __search_all__+"+/"
    __url__ = "www.99comic.com/"

    __book_list__ = []
    __url_list__ = []

    def __init__(self, url, *args, **kwargs):
        super(Download99, self).__init__(url, *args, **kwargs)
        self.__parse__(url)

    def __build_book_list__(self, base, html, url):
        #list = re.findall( self.__host_patterns__ , html)
        list = self.__export_book_to_dict__(base, html)
        for tag in list:
            temp = "http://"+self.__url__+tag[1]
            self.__url_list__.append(temp)
            try:
                name = re.findall(self.__name_patterns__ , tag[0])
            except Exception:
                continue
            #num_list = re.findall(self.__name_patterns__ , name)
            num = ""
            for _ in name:
                num += _
            c99 = Comic99( temp , num)
            c99.Tag = tag[0]
            self.__book_list__.append(c99)
        self.__book_list__ = sorted(self.__book_list__, key=lambda k: k.Name) 
    def __parse__( self , url ):
        compare_url = url.split( self.__url__ )
        if len( compare_url ) is not 2 :
            return False
        base = "comics/"
        page = urllib.urlopen(url)
        html = page.read().decode("utf-8")
        page.close()
        self.__build_book_list__(base, html, url)
        return True
    def List(self):
        return self.__book_list__

