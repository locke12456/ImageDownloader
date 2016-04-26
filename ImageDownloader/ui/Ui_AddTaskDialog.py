# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_AddTaskDialog.ui'
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

class Ui_ComicList(object):
    def setupUi(self, ComicList):
        ComicList.setObjectName(_fromUtf8("ComicList"))
        ComicList.resize(261, 363)
        ComicList.setMinimumSize(QtCore.QSize(261, 363))
        ComicList.setMaximumSize(QtCore.QSize(261, 363))
        self.verticalLayout_2 = QtGui.QVBoxLayout(ComicList)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Radio_SelectAll = QtGui.QRadioButton(ComicList)
        self.Radio_SelectAll.setObjectName(_fromUtf8("Radio_SelectAll"))
        self.horizontalLayout.addWidget(self.Radio_SelectAll)
        self.Radio_Invert = QtGui.QRadioButton(ComicList)
        self.Radio_Invert.setObjectName(_fromUtf8("Radio_Invert"))
        self.horizontalLayout.addWidget(self.Radio_Invert)
        self.Radio_Clear = QtGui.QRadioButton(ComicList)
        self.Radio_Clear.setObjectName(_fromUtf8("Radio_Clear"))
        self.horizontalLayout.addWidget(self.Radio_Clear)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget = QtGui.QListWidget(ComicList)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.buttonBox = QtGui.QDialogButtonBox(ComicList)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ComicList)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ComicList.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ComicList.reject)
        QtCore.QMetaObject.connectSlotsByName(ComicList)

    def retranslateUi(self, ComicList):
        ComicList.setWindowTitle(_translate("ComicList", "Add Task", None))
        self.Radio_SelectAll.setText(_translate("ComicList", "SelectAll", None))
        self.Radio_Invert.setText(_translate("ComicList", "Invert", None))
        self.Radio_Clear.setText(_translate("ComicList", "Clear", None))

