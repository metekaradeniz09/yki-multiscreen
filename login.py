from PyQt5.QtWidgets import *
from login_python import Ui_MainWindow
from YkiPage import YkiPage

class LoginPage(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.loginform = Ui_MainWindow()
        self.loginform.setupUi(self)
        self.YkiPage = YkiPage()
        self.loginform.giris_button.clicked.connect(self.login)
    def login(self):
        kadi = self.loginform.kullaiciadi_value.text()
        sifre = self.loginform.sifre_value.text()
        if kadi == "mete" and sifre == "123" :
            print("Giriş Yapıldı")
            self.YkiPage.show()