# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ImageDownloader.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ImageDownloader(object):
    def setupUi(self, ImageDownloader):
        ImageDownloader.setObjectName(_fromUtf8("ImageDownloader"))
        ImageDownloader.resize(800, 600)
        ImageDownloader.setMinimumSize(QtCore.QSize(800, 600))
        ImageDownloader.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtGui.QWidget(ImageDownloader)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 561))
        self.tabWidget.setMaximumSize(QtCore.QSize(801, 561))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.LineText_ComicUrl = QtGui.QLineEdit(self.tab)
        self.LineText_ComicUrl.setGeometry(QtCore.QRect(80, 40, 551, 20))
        self.LineText_ComicUrl.setObjectName(_fromUtf8("LineText_ComicUrl"))
        self.Label_Url = QtGui.QLabel(self.tab)
        self.Label_Url.setGeometry(QtCore.QRect(0, 40, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Label_Url.setFont(font)
        self.Label_Url.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_Url.setObjectName(_fromUtf8("Label_Url"))
        self.buttonBox = QtGui.QDialogButtonBox(self.tab)
        self.buttonBox.setGeometry(QtCore.QRect(640, 40, 156, 23))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Reset)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.TreeView_ComicLists = QtGui.QTreeWidget(self.tab)
        self.TreeView_ComicLists.setGeometry(QtCore.QRect(0, 70, 791, 421))
        self.TreeView_ComicLists.setObjectName(_fromUtf8("TreeView_ComicLists"))
        self.TreeView_ComicLists.headerItem().setText(0, _fromUtf8("1"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        ImageDownloader.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ImageDownloader)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 17))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        ImageDownloader.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ImageDownloader)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ImageDownloader.setStatusBar(self.statusbar)

        self.retranslateUi(ImageDownloader)
        QtCore.QMetaObject.connectSlotsByName(ImageDownloader)

    def retranslateUi(self, ImageDownloader):
        ImageDownloader.setWindowTitle(_translate("ImageDownloader", "MainWindow", None))
        self.Label_Url.setText(_translate("ImageDownloader", "Comic Url", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ImageDownloader", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ImageDownloader", "Tab 2", None))

