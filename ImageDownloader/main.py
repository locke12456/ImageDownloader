import sys
from PyQt4 import QtGui
from PyQt4.QtCore import Qt
from ImageDownloader import ImageDownloader
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = ImageDownloader()
    myapp.show()
    sys.exit(app.exec_())

