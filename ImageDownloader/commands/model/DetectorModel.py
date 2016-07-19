import os , glob , re
class DetectorModel(object):
    _plugins = None
    
    __search_all__ ="(?:[a-zA-Z]|[0-9])+.py"
    __comic_plugin__ = "Comic"
    __download_plugin__ = "Download"

    """description of class"""
    def __init__(self, *args, **kwargs):
        super(DetectorModel, self).__init__(*args, **kwargs)
        search = [ self.__comic_plugin__ , self.__download_plugin__ ]
        name = glob.glob('plugins/*.py')
        modules = {}
        modules[self.__comic_plugin__] = []
        modules[self.__download_plugin__] = []

        for f in search :
            for file in name:
                ref = f + self.__search_all__
                find_result = re.findall( ref , file )
                if len (find_result) == 1:
                    plugin = str(find_result[0]).replace( ".py" , "" )
                    modules[f].append(plugin) 

        _plugins = map( __import__ , name)
