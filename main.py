import application_initiate
# from views.mainwindow_ui import Ui_MainWindow
# from views.form_ui import Ui_FillOutOfForm
# import sys
# from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QDialog
# from PyQt5.QtCore import Qt

# class FillOutOfForm(QDialog, Ui_FillOutOfForm):
#     def __init__(self, *args, **kwargs):
#         super(FillOutOfForm, self).__init__(*args, **kwargs)
#         self.setupUi(self)

# class MainWindow(QMainWindow, Ui_MainWindow):
#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)
#         self.setupUi(self)
#         self.btn_open.clicked.connect(self.open_dialog)
#         self.btn_cancel.clicked.connect()

#     def open_dialog(self):
#         form = FillOutOfForm()
#         form.show()
#         form.exec()


# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

# app.exec_()