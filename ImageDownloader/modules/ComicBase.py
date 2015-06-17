import urllib , re , socket , os
from modules.IComic import IComic
class ComicBase(IComic):
    """description of class"""
    __search_all__ ="(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))"
    __host_patterns__ = ""
    __pic_patterns__ = ""
    __filename_patterns__ = ""
    __base_url__ = ""
    __pic_list__ = []    
    __host_list__ = []
    url = ""
    num_of_book = ""
    def __init__(self, url , *args, **kwargs):
        return super(ComicBase, self).__init__(*args, **kwargs)
    
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
    
    def Download(self , to_path ):
        raise Exception("not impl")  

