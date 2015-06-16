import urllib
class CommicBase(object):
    """description of class"""
    def __init__(self, url , *args, **kwargs):
        return super(CommicBase, self).__init__(*args, **kwargs)
    def Download(self , to_path ):
        raise Exception("not impl")  

