
import re
from html2text import html2text

class DownloadBase(object):
    """description of class"""

    def __init__(self , url , *args, **kwargs):
        return super(DownloadBase, self).__init__(*args, **kwargs)
    
    def __export_book_to_dict__(self, base, html):
        text = html2text(html)
        l = text.split('[')
        self.__sect_patterns__ = base +self.__sect_patterns__
        list = { (x.split("]")[0],re.findall(self.__sect_patterns__,x)[0]) for x in l if re.findall(self.__sect_patterns__,x) }
        return list
    def List(self):
        #return []
        raise Exception("not impl")  


