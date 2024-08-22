
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sifre_text = QtWidgets.QLabel(self.centralwidget)
        self.sifre_text.setGeometry(QtCore.QRect(260, 220, 101, 20))
        self.sifre_text.setStyleSheet("color: rgb(255, 255, 255);")
        self.sifre_text.setObjectName("sifre_text")
        self.kullancadi_text = QtWidgets.QLabel(self.centralwidget)
        self.kullancadi_text.setGeometry(QtCore.QRect(260, 180, 101, 20))
        self.kullancadi_text.setStyleSheet("color: rgb(255, 255, 255);")
        self.kullancadi_text.setObjectName("kullancadi_text")
        self.kullaiciadi_value = QtWidgets.QLineEdit(self.centralwidget)
        self.kullaiciadi_value.setGeometry(QtCore.QRect(380, 180, 113, 22))
        self.kullaiciadi_value.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.kullaiciadi_value.setObjectName("kullaiciadi_value")
        self.sifre_value = QtWidgets.QLineEdit(self.centralwidget)
        self.sifre_value.setGeometry(QtCore.QRect(380, 220, 113, 22))
        self.sifre_value.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sifre_value.setObjectName("sifre_value")
        self.giris_button = QtWidgets.QPushButton(self.centralwidget)
        self.giris_button.setGeometry(QtCore.QRect(390, 280, 93, 28))
        self.giris_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.giris_button.setObjectName("giris_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sifre_text.setText(_translate("MainWindow", "ŞİFRE:"))
        self.kullancadi_text.setText(_translate("MainWindow", "KULLANICI ADI:"))
        self.giris_button.setText(_translate("MainWindow", "GİRİŞ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
