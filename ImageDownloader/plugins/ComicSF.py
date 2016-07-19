import urllib , re , os
import socket
from ComicBase import ComicBase

class ComicSF(ComicBase):
    """description of class"""
    __search_all__ ="(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))"
    __host_patterns__ = "http[s]?://"+__search_all__+"+"
    __pic_patterns__ = "Pic/"+__search_all__+"+.png"
    __jpg_patterns__ = "Pic/"+__search_all__+"+.JPG"
    __filename_patterns__ = "/"+__search_all__+"+.JPG"
    __js_patterns__ = "/Utility/"+__search_all__+"+"
    __base_url__ = "http://comic.sfacg.com/"
    __pic_list__ = []    
    __host_list__ = []
    
    __class_name__ = "ComicSF"

    @classmethod
    def __register__(self , classname):
        return classname == self.__class_name__

    def __init__(self,  url , nob , *args, **kwargs):
       super(ComicSF, self).__init__(url, *args, **kwargs)
       self.URL = url
       self.Name = nob
    def __parse__(self , url , num_of_book ):
        page = urllib.urlopen(url)
        html = page.read()
        page.close()
        js = self._get_js_file(html, num_of_book)
        self._get_hosts_and_pic(js)

    def _get_js_file(self, html, num_of_book):
        urls = re.findall(self.__js_patterns__ + num_of_book + ".js", html)
        return self.__base_url__ + urls[0]

    def _get_hosts_and_pic(self, js):
        page = urllib.urlopen(js)
        js_file = page.read()
        page.close()
        self.__host_list__ = re.findall(self.__host_patterns__ , js_file)
        self.__pic_list__ = re.findall(self.__jpg_patterns__ , js_file)



    def Download(self, to_path):
        self.__parse__(self.__url__ , self.Name )
        for host in self.__host_list__:
            completed = False
            directory =  to_path + self.Name
            if not os.path.exists(directory):
                os.makedirs(directory , 755)
            completed = self._download_to(host, to_path)
            if completed is not False:
                break
        return completed

