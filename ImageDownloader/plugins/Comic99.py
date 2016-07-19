import urllib , re , os
import socket
from ComicBase import ComicBase

class Comic99(ComicBase):
    """description of class"""
    __search_all__ ="(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))"
    __host_patterns__ = "(?:[0-9])+"
    __pic_patterns__ = "/ok-comic"+__search_all__+"+.JPG"
    __filename_patterns__ = "/"+__search_all__+"+.JPG"
    __base_url__ = ""
    __pic_list__ = []    
    __host_list__ = ["http://99.1112223333.com/dm"]
    
    __class_name__ = "Comic99"

    @classmethod
    def __register__(self , classname):
        return classname == self.__class_name__


    def __init__(self,  url , nob , *args, **kwargs):
       super(Comic99, self).__init__(url, *args, **kwargs)
       self.URL = url
       self.Name = nob
    def __parse__(self , url , num_of_book ):
        page = urllib.urlopen(url)
        html = page.read()
        page.close()
        self._get_hosts_and_pic(html)


    def _get_hosts_and_pic(self, html):
        self.__pic_list__ = re.findall(self.__pic_patterns__ , html)
        self.__base_url__ = re.findall(self.__host_patterns__ , self.__pic_list__[0])[0]


    def Download(self, to_path):
        self.__parse__(self.__url__ , self.Name )
        for host in self.__host_list__:
            completed = False
            host += self.__base_url__
            directory =  to_path + self.Name
            if not os.path.exists(directory):
                os.makedirs(directory , 755)
            completed = self._download_to(host, to_path)
            if completed is not False:
                break
        return completed