from views.caculator_ui import Ui_MainCaculator
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QDialog
from PyQt5.QtCore import Qt

class MainCaculator(QMainWindow, Ui_MainCaculator):
    def __init__(self, *args, **kwargs):
        super(MainCaculator, self).__init__(*args, **kwargs)
        self.setupUi(self)