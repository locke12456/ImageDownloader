
import re
from html2text import html2text

class DownloadBase(object):
    """description of class"""
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

    def __init__(self , url , *args, **kwargs):
        return super(DownloadBase, self).__init__(*args, **kwargs)
    
    def __get_comic_name__(self,html):
        text = html2text(html)
        l = text.split('[')
        list = { (x.split("]")[0],re.findall(self.__comic_name_patterns__,x)[0]) for x in l if re.findall(self.__comic_name_patterns__,x) }
        return list

    def __export_book_to_dict__(self, base, html):
        text = html2text(html)
        l = text.split('[')
        self.__sect_patterns__ = base +self.__sect_patterns__
        list = { (x.split("]")[0],re.findall(self.__sect_patterns__,x)[0]) for x in l if re.findall(self.__sect_patterns__,x) }
        return list
    def List(self):
        #return []
        raise Exception("not impl")  


