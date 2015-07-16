from ui.Ui_ImageDownloader import Ui_ImageDownloader
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QTreeWidgetItem, QDialogButtonBox
from GuiItems.DownloadItemBase import DownloadItemBase
from modules.DownloadSF import DownloadSF
from modules.Download99 import Download99


class ImageDownloader(QtGui.QMainWindow, Ui_ImageDownloader):
    focusIn = QtCore.pyqtSignal(QtCore.QObject)
    focusItem = None
    def __init__(self, parent=None):
       QtGui.QWidget.__init__(self, parent)
       
       self.setupUi(self)
       #self.LineText_ComicUrl.focusInEvent = self.focusInEvent
       self.LineText_ComicUrl.keyPressEvent = self.keyPressEvent
       #self.TreeView_ComicLists.se
       #self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.call)
       #item = DownloadItemBase(self.TreeView_ComicLists)
       #item.setText(0, "comic")
       #self.TreeView_ComicLists.addTopLevelItem(item)
       #item2 = DownloadItemBase(item)
       #item2.setText(0, "comic")
       #item.addChild(item2)
    def call(self):
        item = DownloadItemBase(self.TreeView_ComicLists)
        sf = DownloadSF(str(self.LineText_ComicUrl.text())) 
        item.setText(0, sf.Name)
        ComicList = sf.List()
        for comic in ComicList:
            item2 = DownloadItemBase(item)
            item2.setText(0,  comic.Tag )
            item.addChild(item2)
            
            print comic.Name + " : " + comic.URL
        self.TreeView_ComicLists.addTopLevelItem(item)
    @QtCore.pyqtSlot(QtCore.QObject)
    def focusInEvent(self, event):
        event
        pass
    @QtCore.pyqtSlot(QtCore.QObject)
    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Enter :
            self.call()
            pass
        event.accept()
    @QtCore.pyqtSlot(QtCore.QObject)
    def contextMenuEvent(self, event):
        #super(ImageDownloader,self).contextMenuEvent(self,event)
        if self.TreeView_ComicLists.SelectRows == 1:
            menu = QtGui.QMenu(self)
            menu.addAction(self.actionDownload)
            if(self.TreeView_ComicLists.SelectColumns < 1):
                self.actionDownload.setDisabled(True)
            menu.addAction(self.actionSelecet_All)
            menu.addAction(self.actionUnselecet_All)
            menu.addAction(self.actionCancel)
            self.menu = menu
            self.menu.popup(QtGui.QCursor.pos())
    
    @QtCore.pyqtSlot(QtCore.QObject)
    def renameSlot(self, event):
        pass
