from DownloadBase import DownloadBase
from ComicBase import ComicBase , urllib
import re
from modules.Comic99 import Comic99
class Download99(DownloadBase):
    """description of class"""
    __search_all__ ="(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))"
    __host_patterns__ = "comics/"+__search_all__+"+/"
    __name_patterns__ = '[0-9]'
    __url__ = "www.99comic.com/"

    __book_list__ = []
    __url_list__ = []

    def __init__(self, url, *args, **kwargs):
        super(Download99, self).__init__(url, *args, **kwargs)
        self.__parse__(url)

    def __build_book_list__(self, base, html, url):
        list = re.findall( self.__host_patterns__ , html)

        for tag in list:
            temp = "http://"+self.__url__+tag
            self.__url_list__.append(temp)
            try:
                name = html.split(tag)[1].split("</a>")[0].split("'>")[1]
            except Exception:
                continue
            num_list = re.findall(self.__name_patterns__ , name)
            num = ""
            for _ in num_list:
                num += _
            sf = Comic99( temp , num)
            self.__book_list__.append(sf)

    def __parse__( self , url ):
        compare_url = url.split( self.__url__ )
        if len( compare_url ) is not 2 :
            return False
        base = compare_url[1]
        page = urllib.urlopen(url)
        html = page.read()
        page.close()
        self.__build_book_list__(base, html, url)
        return True
    def List(self):
        return self.__book_list__

