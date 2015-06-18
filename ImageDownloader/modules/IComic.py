class IComic(object):
    """description of class"""
    __name__ = ""
    __url__ =""
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

    def Download(self , to_path ):
        raise Exception("not impl") 