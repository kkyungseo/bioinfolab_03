import sys
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, uic

form_class = uic.loadUiType("mainWindow.ui")[0]
currentPath = os.getcwd()
class NewMain(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.kmplot_btn.clicked.connect(self.openSurvival)
        self.cross_btn.clicked.connect(self.openCRISPR)
        self.sample_btn.clicked.connect(self.openDrug)
        #statusBar which shows License Number(in this case, 'abcd')
        self.statusBar().showMessage('abcd')

    def openSurvival(self):
        self.os = survival()
        self.os.show()

    def openCRISPR(self):
        self.oc = crispr()
        self.oc.show()

    def openDrug(self):
        self.od = drug()
        self.od.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = NewMain()
    myWindow.show()
    app.exec_()

