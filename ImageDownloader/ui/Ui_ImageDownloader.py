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
        ImageDownloader.resize(521, 553)
        ImageDownloader.setMinimumSize(QtCore.QSize(0, 0))
        ImageDownloader.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtGui.QWidget(ImageDownloader)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 521, 501))
        self.tabWidget.setMaximumSize(QtCore.QSize(801, 561))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.frame = QtGui.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(0, 0, 521, 471))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.TreeView_ComicLists = QtGui.QTreeWidget(self.frame)
        self.TreeView_ComicLists.setGeometry(QtCore.QRect(0, 40, 511, 421))
        self.TreeView_ComicLists.setObjectName(_fromUtf8("TreeView_ComicLists"))
        self.TreeView_ComicLists.headerItem().setText(0, _fromUtf8("1"))
        self.LineText_ComicUrl = QtGui.QLineEdit(self.frame)
        self.LineText_ComicUrl.setGeometry(QtCore.QRect(40, 10, 471, 20))
        self.LineText_ComicUrl.setObjectName(_fromUtf8("LineText_ComicUrl"))
        self.Label_Url = QtGui.QLabel(self.frame)
        self.Label_Url.setGeometry(QtCore.QRect(0, 10, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Label_Url.setFont(font)
        self.Label_Url.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Url.setObjectName(_fromUtf8("Label_Url"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        ImageDownloader.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(ImageDownloader)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ImageDownloader.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(ImageDownloader)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        ImageDownloader.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtGui.QToolBar(ImageDownloader)
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        ImageDownloader.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.actionNewTask = QtGui.QAction(ImageDownloader)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Milky/Icons/64/112.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionNewTask.setIcon(icon)
        self.actionNewTask.setObjectName(_fromUtf8("actionNewTask"))
        self.actionSearch = QtGui.QAction(ImageDownloader)
        self.actionSearch.setEnabled(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Milky/Icons/64/10.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionSearch.setIcon(icon1)
        self.actionSearch.setObjectName(_fromUtf8("actionSearch"))
        self.actionOptions = QtGui.QAction(ImageDownloader)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Milky/Icons/64/11.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionOptions.setIcon(icon2)
        self.actionOptions.setObjectName(_fromUtf8("actionOptions"))
        self.actionUnselecet_All = QtGui.QAction(ImageDownloader)
        self.actionUnselecet_All.setObjectName(_fromUtf8("actionUnselecet_All"))
        self.actionSelecet_All = QtGui.QAction(ImageDownloader)
        self.actionSelecet_All.setObjectName(_fromUtf8("actionSelecet_All"))
        self.actionDownload = QtGui.QAction(ImageDownloader)
        self.actionDownload.setObjectName(_fromUtf8("actionDownload"))
        self.actionCancel = QtGui.QAction(ImageDownloader)
        self.actionCancel.setObjectName(_fromUtf8("actionCancel"))
        self.toolBar.addAction(self.actionNewTask)
        self.toolBar_2.addAction(self.actionSearch)
        self.toolBar_2.addAction(self.actionOptions)

        self.retranslateUi(ImageDownloader)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ImageDownloader)

    def retranslateUi(self, ImageDownloader):
        ImageDownloader.setWindowTitle(_translate("ImageDownloader", "ImageDownloader", None))
        self.Label_Url.setText(_translate("ImageDownloader", "Url", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ImageDownloader", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ImageDownloader", "Tab 2", None))
        self.toolBar.setWindowTitle(_translate("ImageDownloader", "toolBar", None))
        self.toolBar_2.setWindowTitle(_translate("ImageDownloader", "toolBar_2", None))
        self.actionNewTask.setText(_translate("ImageDownloader", "NewTask", None))
        self.actionSearch.setText(_translate("ImageDownloader", "Search", None))
        self.actionOptions.setText(_translate("ImageDownloader", "Options", None))
        self.actionUnselecet_All.setText(_translate("ImageDownloader", "Unselecet All", None))
        self.actionSelecet_All.setText(_translate("ImageDownloader", "Selecet All", None))
        self.actionDownload.setText(_translate("ImageDownloader", "Download", None))
        self.actionCancel.setText(_translate("ImageDownloader", "Cancel", None))

import umleditor_rc
