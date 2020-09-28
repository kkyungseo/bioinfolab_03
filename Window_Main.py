import sys
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QComboBox, QFrame, QLabel, QGroupBox, QToolButton, QStatusBar, QApplication
from PyQt5 import QtCore, uic
from Window_Survival import SurvivalSearchWindow
from Window_CrossAnalysis import CAMainWindow
from Window_2Dplot import TwoDistWindow

form_class = uic.loadUiType("GUI/mainWindow.ui")[0]
currentPath = os.getcwd()

# block errors of Window_Main
def my_exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)

class MainWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        sys.excepthook = my_exception_hook  # pyqt5 exception
        self.setupUi(self)
        self.initUI()

# comboboxes of 'Create project'
    def initUI(self):
        self.radio_patient.toggled.connect(self.analysis_type)
        self.radio_cell.toggled.connect(self.analysis_type)

        self.combo_analysis.currentIndexChanged.connect(self.dataset_type)

        self.btn_survival.clicked.connect(self.openSurvival)
        self.btn_cross.clicked.connect(lambda: self.openCRISPR("sgRNA", "genes"))
        self.btn_scatter.clicked.connect(lambda: self.open2Dist("Gene", "Drug"))

        self.btn_create.clicked.connect(self.openWindow)

        self.statusBar().showMessage('CBiS')

#radio buttons
    def analysis_type(self):
        if self.radio_patient.isChecked(True):
            self.combo_analysis.clear()
            self.combo_analysis.addItems(["(Select analysis)", "Survival plots"])
        elif self.radio_cell.isChecked(True):
            self.combo_analysis.clear()
            self.combo_analysis.addItems(["(Select analysis)", "Cross-association", "Scatter 2D/3D plots", "Box plot"])

# choice of combo_analysis changes the content of combo_dataset2
    def dataset_type(self):

        if self.combo_analysis.currentText() == "Survival plots":
            self.combo_query.clear()
            self.combo_query.addItems(["(Dataset1)", "Gene expression"])
            self.combo_target.clear()
            self.combo_target.addItems(["(Dataset2)","Patient Survival"])
        elif self.combo_analysis.currentText() == "Cross-association":
            self.combo_query.clear()
            self.combo_query.addItems(["(Dataset1)", "Genes expression", "Drugs screen", "sgRNAs screen"])
            self.combo_target.clear()
            self.combo_target.addItems(["(Dataset2)", "Gene expression", "Drug screen", "sgRNA screen"])
        elif self.combo_analysis.currentText() == "Scatter 2D/3D plots":
            self.combo_query.clear()
            self.combo_query.addItems(["(Dataset1)", "Gene expression", "Drug screen", "sgRNA screen"])
            self.combo_target.clear()
            self.combo_target.addItems(["(Dataset2)", "Gene expression", "Drug screen", "sgRNA screen"])
        elif self.combo_analysis.currentText() == "Box plot":
            self.combo_query.clear()
            self.combo_query.addItems(["(Dataset1)", "Gene expression", "Drug screen", "sgRNA screen"])
            self.combo_target.clear()
            self.combo_target.addItems(["(Dataset2)", "Gene expression", "Drug screen", "sgRNA screen"])

# connect windows according to combo_analysis
    def openWindow(self):

        if self.combo_target.currentText() == "Patient Survival":
            self.openSurvival()

        #cross-analysis
        elif self.combo_analysis.currentText() == "Cross-association":

            if self.combo_target.currentText() == "Gene expression":
                data1 = "gene"
            elif self.combo_target.currentText() == "Drug screen":
                data1 = "drug"
            elif self.combo_target.currentText() == "sgRNA screen":
                data1 = "sgRNA"

            if self.combo_query.currentText() == "Genes expression":
                data2 = "genes"
            elif self.combo_query.currentText() == "Drugs screen":
                data2 = "drugs"
            elif self.combo_query.currentText() == "sgRNAs screen":
                data2 = "sgRNAs"
            self.openCRISPR(data2, data1)

        elif self.combo_analysis.currentText() == "Scatter 2D/3D plots":

            if self.combo_query.currentText() == "Gene expression":
                data1 = "Gene"
            elif self.combo_query.currentText() == "Drug screen":
                data1 = "Drug"
            elif self.combo_query.currentText() == "sgRNA screen":
                data1 = "sgRNA"

            if self.combo_target.currentText() == "Gene expression":
                data2 = "Gene"
            elif self.combo_target.currentText() == "Drug screen":
                data2 = "Drug"
            elif self.combo_target.currentText() == "sgRNA screen":
                data2 = "sgRNA"
            self.open2Dist(data1,data2)

# connect functions to quick start menus
    def openSurvival(self):
        # self.os = SelectLineageWindow()
        self.os = SurvivalSearchWindow()
        self.os.show()

    def openCRISPR(self, d, c):
        self.oc = CAMainWindow(d, c)
        self.oc.show()

    def open2Dist(self, a, b):
        self.od = TwoDistWindow(a, b)
        self.od.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_()
