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

