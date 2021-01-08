from views.mainwindow_ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QDialog
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)