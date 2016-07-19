import os , glob , re
from plugins.ComicBase import ComicBase
from plugins.DownloadBase import DownloadBase
class PluginLoader(object):
    """description of class"""
    _plugins = None    
    __search_all__ ="(?:[a-zA-Z]|[0-9])+.py"
    __comic_plugin__ = "Comic"
    __download_plugin__ = "Download"
    _modules = None
    """description of class"""

    def Plugins(self):
        return self._modules

    def __init__(self, *args, **kwargs):
        super(PluginLoader, self).__init__(*args, **kwargs)
        
        search = [ self.__comic_plugin__ , self.__download_plugin__ ]
        
        name = glob.glob('plugins/*.py')
        
        modules, modules_name = self.__init_mapping_plugins__(name, search)

        self._plugins = map( __import__ , modules_name )

        self.__init_mapping_classes__(modules)


    def __init_mapping_plugins__(self, name, search):
        modules = {}
        modules[self.__comic_plugin__] = []
        modules[self.__download_plugin__] = []
        
        self._modules = {}
        self._modules[self.__comic_plugin__] = {}
        self._modules[self.__download_plugin__] = {}
        
        modules_name = []
        for f in search :
            for file in name:
                ref = f + self.__search_all__
                find_result = re.findall( ref , file )
                if len (find_result) == 1:
                    plugin = str(find_result[0]).replace( ".py" , "" )
                    modules[f].append(plugin) 
                    modules_name.append("plugins."+plugin)
        return modules, modules_name

    def __init_mapping_classes__(self, modules):
        baseclass = {}
        baseclass[self.__comic_plugin__] = ComicBase
        baseclass[self.__download_plugin__] = DownloadBase
        for key,plugins in modules.iteritems():
            for plugin in plugins:
                for cls in baseclass[key].__subclasses__():
                    if cls.__register__(plugin):
                        self._modules[key][plugin] = cls

