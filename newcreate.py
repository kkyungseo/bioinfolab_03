import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore
from mainfail import MainFailClass
form_class = uic.loadUiType("newcreate.ui")[0]

class NewCreate(QDialog, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('New Project')


 ***QComboBox가 작동하게 하기 (각각의 lineage와 연결되게 만들기 - OK 버튼을 눌러야 연결이 되는 것)