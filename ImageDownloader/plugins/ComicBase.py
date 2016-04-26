import urllib , re , socket , os
from plugins.IComic import IComic
class ComicBase(IComic):
    """description of class"""
    __search_all__ ="(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))"
    __host_patterns__ = ""
    __pic_patterns__ = ""
    __filename_patterns__ = ""
    __base_url__ = ""
    __pic_list__ = []    
    __host_list__ = []
    __retry__ = 1
    

### properties

    __name__ = ""
    __url__ =""
    __tag__ =""
    
    @property 
    def Tag(self):
        return self.__tag__
    @Tag.setter
    def Tag(self,value):
        self.__tag__ = value
    @property 
    def Name(self):
        return self.__name__
    @Name.setter
    def Name(self,value):
        self.__name__ = value    
    @property 
    def URL(self):
        return self.__url__
    @URL.setter
    def URL(self,value):
        self.__url__ = value
    def __init__(self, url , *args, **kwargs):
        return super(ComicBase, self).__init__(*args, **kwargs)


    
    def _download_file(self, file, url):
        retry = self.__retry__
        while retry > 0 :
            try : 
                socket.setdefaulttimeout(10)
                urllib.urlretrieve(url , file)
            except Exception as e:
                print e.message
            retry-=1

    def _download_to(self, host, to_path):
    
        completed = False
        for pic_url in self.__pic_list__:
            url =  host +"/"+ pic_url
            file = re.findall(self.Name+self.__filename_patterns__ , pic_url)[0]
            file =  to_path + file
            self._download_file(file, url)
            completed = os.path.isfile(file)
            if completed is not True:
                break
        return completed
    
    def setRetry(self , value):
        self.__retry__ = value

    def Download(self , to_path ):
        raise Exception("not impl")  

