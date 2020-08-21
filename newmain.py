import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore
from mainfail import MainFailClass
form_class = uic.loadUiType("newmain.ui")[0]

class NewMain(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):

        #Create of menubar (create 를 누르면 'New project' 창이 뜨도록하기 )

        #Exit of menubar(self가 붙는지 안 붙는지 다시 확인하기 )
        actionExit = QAction('&Exit', self)
        actionExit.setShortcut('Ctrl+Q')
        actionExit.setStatusTip('Exit Application')
        actionExit.triggered.connect(qApp.quit)

        #drag n drop within list(이름 통일 & 기능 확인하기)

        # enabled the drag and drop facility for our two QListWidgets
        self.patient_list = QListWidget()
        self.cell_list = QListWidget()
        self.cell_list.setViewMode(QListWidget.IconMode)
        self.patient_list.setAcceptDrops(True)
        self.patient_list.setDragEnabled(True)
        self.cell_list.setAcceptDrops(True)
        self.cell_list.setDragEnabled(True)

        self.setGeometry(300, 350, 500, 300)
        self.myLayout = QHBoxLayout()
        self.myLayout.addWidget(self.patient_list)
        self.myLayout.addWidget(self.cell_list)

        #add items to two QListWidgets to make sure to have some icons in working directoru
        l1 = QListWidgetItem(QIcon('drugpng'), "Drug&Chemicals")
        l2 = QListWidgetItem(QIcon('CRISPR.png'), "CRISPR(sgRNA)")
        l3 = QListWidgetItem(QIcon('shRNA.png'), "shRNA knockdown")
        l4 = QListWidgetItem(QIcon('mRNA.png'), "Gene(mRNA)expression")
        self.patient_list.insertItem(1, l1)
        self.patient_list.insertItem(2, l2)
        self.patient_list.insertItem(3, l3)
        self.myListWidget1.insertItem(4, l4)

        #위의 아이콘과 아래 세 개의 아이콘 차이 (몇 번쨰 리스트인지가 관련이 있을 듯)

        QListWidgetItem(QIcon('html.png'), "HTLM", self.
                        cell_list)
        QListWidgetItem(QIcon('css.png'), "CSS", self.
                        cell_list)
        QListWidgetItem(QIcon('javascript.png'), "Javascript", self.
                        cell_list)

        self.setWindowTitle('Qomics');
        self.setLayout(self.myLayout)

        self.show()


        #statusBar which shows License Number(in this case, 'abcd')
        self.statusBar().showMessage('abcd')

        self.setGeometry(200, 100, 800, 530)

        self.show()




#구조 참고하기
    #def openCellLineWindow(self):
        #try:
           #open_CellLineWindow = scatterWindow()
           #open_CellLineWindow.show()
       # except:
            #open_fail = MainFailClass()
            #open_fail.show()