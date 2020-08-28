import sys
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, uic

form_class = uic.loadUiType("newopenv2.ui")[0]
currentPath = os.getcwd()
class NewMain(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Qomics")

    def initUI(self):

        # enabled the drag and drop facility for our two QListWidgets
        self.lineage_list = QListWidget()
        self.patient_list = QListWidget()
        self.cell_list = QListWidget()

        self.drop_list.setViewMode(QListWidget.IconMode)


        self.setLayout(self.myLayout)

        self.show()


        #statusBar which shows License Number(in this case, 'abcd')
        self.statusBar().showMessage('abcd')

        self.setGeometry(200, 100, 800, 530)

        self.show()

    #action methods of Go buttons of MainWindow
    # adding actions to buttons
    #(여기에 이제 create 제외하고 세 가지 기능을 연결하면됩니다!)

    def kmplot_clicked(self):


        self.kmplot_btn.clicked.connect(self.kmplot_clicked)

    def cross_clicked(self):

        self.cross_btn.clicked.connect(self.cross_clicked)

    def sample_clicked(self):


        self.sample_btn.clicked.connect(self.sample_clicked)

    def create_clicked(self):


        self.create_btn.clicked.connect(self.create_clicked)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = NewMain()
    myWindow.show()
    app.exec_()

