from PyQt5.QtWidgets import *
from yki_python import Ui_MainWindow

class YkiPage (QMainWindow):
    def __init__(self):
        super().__init__()
        self.ykiform = Ui_MainWindow()
        self.ykiform.setupUi(self)

