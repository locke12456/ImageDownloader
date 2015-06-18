from DownloadBase import DownloadBase
from ComicBase import ComicBase , urllib
from modules.ComicSF import ComicSF
import re
class DownloadSF(DownloadBase):
    """description of class"""
    __search_all__ ="(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))"
    __host_patterns__ = __search_all__+"+/"

    __url__ = "comic.sfacg.com/"

    __book_list__ = []
    __url_list__ = []

    def __init__(self, url, *args, **kwargs):
        super(DownloadSF, self).__init__(url, *args, **kwargs)
        self.__parse__(url)

    def __build_book_list__(self, base, html, url):
        list = re.findall(base + self.__host_patterns__ , html)
        for tag in list:
            sect = tag.split(base)
            temp = sect[1].split("/")
            tempurl = url+sect[1]
            self.__url_list__.append(tempurl)
            sf = ComicSF(tempurl , temp[0])
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

