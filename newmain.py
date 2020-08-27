import sys
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, uic

form_class = uic.loadUiType("newmain.ui")[0]
currentPath = os.getcwd()
class NewMain(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


    def initUI(self):

        #exit of menubar
        quit_action = QAction('Exit', self)
        quit_action.setShortcut('Crtl+Q')


        # enabled the drag and drop facility for our two QListWidgets
        self.lineage_list = QListWidget()
        self.patient_list = QListWidget()
        self.cell_list = QListWidget()
        self.drop_list = QListWidget()

        self.drop_list.setViewMode(QListWidget.IconMode)

        self.lineage_list.setAcceptDrops(True)
        self.lineage_list.setDragEnabled(True)
        self.patient_list.setAcceptDrops(True)
        self.patient_list.setDragEnabled(True)
        self.cell_list.setAcceptDrops(True)
        self.cell_list.setDragEnabled(True)

        self.setGeometry(300, 350, 500, 300)

        #add items to two QListWidgets to make sure to have some icons in working directoru
        l1 = QListWidgetItem(QIcon('colon.png'), "Colon")
        l2 = QListWidgetItem(QIcon('lung.png'), "Lung")
        l3 = QListWidgetItem(QIcon('leukemia.png'), "Leukemia")
        l4 = QListWidgetItem(QIcon('liver.png'), "Liver")
        l5 = QListWidgetItem(QIcon('survival.png'), "Survival")
        l6 = QListWidgetItem(QIcon('geneexpression.png'), "Gene(mRNA) expression")
        l7 = QListWidgetItem(QIcon('drug.png'), "Drug & Chemicals")
        l8 = QListWidgetItem(QIcon('sgRNA.png'), "CRISPR(sgRNA)")
        l9 = QListWidgetItem(QIcon('shRNA.png'), "shRHA knockdown")
        l10 = QListWidgetItem(QIcon('mRNA.png'), "Gene(mRNA) expression")

        self.lineage_list.insertItem(0, l1)
        self.lineage_list.insertItem(1, l2)
        self.lineage_list.insertItem(2, l3)
        self.lineage_list.insertItem(3, l4)

        self.patient_list.insertItem(0, l5)
        self.patient_list.insertItem(1, l6)

        self.cell_list.insertItem(0, l7)
        self.cell_list.insertItem(1, l8)
        self.cell_list.insertItem(2, l9)
        self.cell_list.insertItem(3, l10)

        QListWidgetItem(QIcon('colon.png'), "HTLM", self.drop_list)




        self.setWindowTitle('Qomics');
        self.setLayout(self.myLayout)

        self.show()


        #statusBar which shows License Number(in this case, 'abcd')
        self.statusBar().showMessage('abcd')

        self.setGeometry(200, 100, 800, 530)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = NewMain()
    myWindow.show()
    app.exec_()

