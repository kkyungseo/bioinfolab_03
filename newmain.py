import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, uic

form_class = uic.loadUiType("newmain.ui")[0]

class NewMain(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.aceept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLicalFile()))
            self.emit(QtCore.SIGNALS("dropped"),links)
        else:
            event.ignore()

    def initUI(self):

        #Exit of menubar(self가 붙는지 안 붙는지 다시 확인하기 )
        actionExit = QAction('&Exit', self)
        actionExit.setShortcut('Ctrl+Q')
        actionExit.setStatusTip('Exit Application')
        actionExit.triggered.connect(qApp.quit)

        #drag n drop within list(이름 통일 & 기능 확인하기)

        #LINEAGE도 이제 리스트로 추가되었음

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

        self.setWindowTitle('Qomics');
        self.setLayout(self.myLayout)

        self.show()


        #statusBar which shows License Number(in this case, 'abcd')
        self.statusBar().showMessage('abcd')

        self.setGeometry(200, 100, 800, 530)

        self.show()


