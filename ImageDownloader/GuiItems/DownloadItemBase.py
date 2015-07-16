from PyQt4.QtCore import Qt
from PyQt4.QtGui import QTreeWidgetItem
class DownloadItemBase(QTreeWidgetItem):
    """description of class"""
    __name__ = ""
    __state__  = False
    def __init__(self , parent, *args):
        
        super(DownloadItemBase, self ).__init__(parent , *args)
        self.setText(0, "comic")
        self.setCheckState(0,Qt.Unchecked)
        self.setFlags( Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
    @property 
    def Name(self):
        return self.__name__
    @Name.setter 
    def Name(self,value):
        self.__name__ = value
    @property
    def State(self):
        return self.__state__
    @State.setter 
    def State(self,value):
        self.__state__ = value
    
