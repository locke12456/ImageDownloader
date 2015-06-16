import urllib , re , os
import socket
from CommicBase import CommicBase

class CommicSF(CommicBase):
    """description of class"""
    __search_all__ ="(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))"
    __host_patterns__ = "http[s]?://"+__search_all__+"+"
    __pic_patterns__ = "Pic/"+__search_all__+"+.png"
    __filename_patterns__ = "/"+__search_all__+"+.png"
    __js_patterns__ = "/Utility/"+__search_all__+"+"
    __base_url__ = "http://comic.sfacg.com/"
    __pic_list__ = []    
    __host_list__ = []
    url = ""
    num_of_book = ""
    def __init__(self,  url , nob , *args, **kwargs):
       super(CommicSF, self).__init__(url, *args, **kwargs)
       self.url = url
       self.num_of_book = nob
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
        self.__pic_list__ = re.findall(self.__pic_patterns__ , js_file)

    def _download_to(self, host, to_path):
        completed = False
        for pic_url in self.__pic_list__:
            url =  host +"/"+ pic_url
            file = re.findall(self.num_of_book+self.__filename_patterns__ , pic_url)[0]
            file =  to_path + file
            try : 
                socket.setdefaulttimeout(10)
                urllib.urlretrieve(url , file)
            except Exception:
                return False
            completed = os.path.isfile(file)
            if completed is not True:
                break
        return completed
                    

    def Download(self, to_path):
        self.__parse__(self.url , self.num_of_book )
        for host in self.__host_list__:
            completed = False
            directory =  to_path + self.num_of_book
            if not os.path.exists(directory):
                os.makedirs(directory , 755)
            completed = self._download_to(host, to_path)
            if completed is not False:
                break
        return completed

