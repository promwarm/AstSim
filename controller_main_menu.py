from PyQt5 import QtWidgets
import sys
import view_main_menu
import view_settings


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = view_main_menu.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_settings.clicked.connect(self.settings)

    def settings(self):
        self.window = QtWidgets.QDialog()
        self.settings_ui = view_settings.Ui_Dialog()
        print("It works so far..")
        self.settings_ui.setupUi(window)
        self.window.show()


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())