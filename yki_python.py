import time
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from PyQt5 import QtCore, QtGui, QtWidgets
from dronekit import *
import time
from datetime import datetime


connection_string = "127.0.0.1:14550"
vehicle = connect(connection_string, wait_ready=False)


class Ui_MainWindow(object):




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1252, 784)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.arm_button = QtWidgets.QPushButton(self.centralwidget)
        self.arm_button.setGeometry(QtCore.QRect(430, 480, 93, 28))
        self.arm_button.setObjectName("arm_button")
        self.disarm_button = QtWidgets.QPushButton(self.centralwidget)
        self.disarm_button.setGeometry(QtCore.QRect(540, 480, 93, 28))
        self.disarm_button.setObjectName("disarm_button")
        self.manuel_button = QtWidgets.QPushButton(self.centralwidget)
        self.manuel_button.setGeometry(QtCore.QRect(650, 480, 93, 28))
        self.manuel_button.setObjectName("manuel_button")
        self.stailize_button = QtWidgets.QPushButton(self.centralwidget)
        self.stailize_button.setGeometry(QtCore.QRect(430, 520, 93, 28))
        self.stailize_button.setObjectName("stailize_button")
        self.auto_button = QtWidgets.QPushButton(self.centralwidget)
        self.auto_button.setGeometry(QtCore.QRect(650, 520, 93, 28))
        self.auto_button.setObjectName("auto_button")
        self.guided_button = QtWidgets.QPushButton(self.centralwidget)
        self.guided_button.setGeometry(QtCore.QRect(540, 520, 93, 28))
        self.guided_button.setObjectName("guided_button")
        self.loitter_button = QtWidgets.QPushButton(self.centralwidget)
        self.loitter_button.setGeometry(QtCore.QRect(430, 560, 93, 28))
        self.loitter_button.setObjectName("loitter_button")
        self.gorev_button = QtWidgets.QPushButton(self.centralwidget)
        self.gorev_button.setGeometry(QtCore.QRect(650, 560, 93, 28))
        self.gorev_button.setObjectName("gorev_button")
        self.rtl_button = QtWidgets.QPushButton(self.centralwidget)
        self.rtl_button.setGeometry(QtCore.QRect(540, 560, 93, 28))
        self.rtl_button.setObjectName("rtl_button")
        self.ip_value = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_value.setGeometry(QtCore.QRect(1120, 10, 113, 21))
        self.ip_value.setObjectName("ip_value")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(1120, 50, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.ip_text = QtWidgets.QLabel(self.centralwidget)
        self.ip_text.setGeometry(QtCore.QRect(1050, 10, 55, 16))
        self.ip_text.setObjectName("ip_text")
        self.baud_text = QtWidgets.QLabel(self.centralwidget)
        self.baud_text.setGeometry(QtCore.QRect(1050, 50, 55, 16))
        self.baud_text.setObjectName("baud_text")
        self.altitude_value = QtWidgets.QLabel(self.centralwidget)
        self.altitude_value.setGeometry(QtCore.QRect(130, 0, 55, 16))
        self.altitude_value.setObjectName("altitude_value")
        self.airspeed_value = QtWidgets.QLabel(self.centralwidget)
        self.airspeed_value.setGeometry(QtCore.QRect(130, 30, 55, 16))
        self.airspeed_value.setObjectName("airspeed_value")
        self.gpsspeed_value = QtWidgets.QLabel(self.centralwidget)
        self.gpsspeed_value.setGeometry(QtCore.QRect(130, 60, 55, 16))
        self.gpsspeed_value.setObjectName("gpsspeed_value")
        self.distance_value = QtWidgets.QLabel(self.centralwidget)
        self.distance_value.setGeometry(QtCore.QRect(130, 90, 55, 16))
        self.distance_value.setObjectName("distance_value")
        self.throotle_value = QtWidgets.QLabel(self.centralwidget)
        self.throotle_value.setGeometry(QtCore.QRect(130, 180, 55, 16))
        self.throotle_value.setObjectName("throotle_value")
        self.roll_value = QtWidgets.QLabel(self.centralwidget)
        self.roll_value.setGeometry(QtCore.QRect(130, 120, 55, 16))
        self.roll_value.setObjectName("roll_value")
        self.yaw_value = QtWidgets.QLabel(self.centralwidget)
        self.yaw_value.setGeometry(QtCore.QRect(130, 150, 55, 16))
        self.yaw_value.setObjectName("yaw_value")
        self.gpscount_value = QtWidgets.QLabel(self.centralwidget)
        self.gpscount_value.setGeometry(QtCore.QRect(130, 210, 55, 16))
        self.gpscount_value.setObjectName("gpscount_value")
        self.gpsspeed_text = QtWidgets.QLabel(self.centralwidget)
        self.gpsspeed_text.setGeometry(QtCore.QRect(30, 60, 81, 16))
        self.gpsspeed_text.setObjectName("gpsspeed_text")
        self.yaw_text = QtWidgets.QLabel(self.centralwidget)
        self.yaw_text.setGeometry(QtCore.QRect(30, 150, 81, 16))
        self.yaw_text.setObjectName("yaw_text")
        self.altitude_text = QtWidgets.QLabel(self.centralwidget)
        self.altitude_text.setGeometry(QtCore.QRect(30, 0, 81, 16))
        self.altitude_text.setObjectName("altitude_text")
        self.airspeed_text = QtWidgets.QLabel(self.centralwidget)
        self.airspeed_text.setGeometry(QtCore.QRect(30, 30, 81, 16))
        self.airspeed_text.setObjectName("airspeed_text")
        self.distance_text = QtWidgets.QLabel(self.centralwidget)
        self.distance_text.setGeometry(QtCore.QRect(30, 90, 81, 16))
        self.distance_text.setObjectName("distance_text")
        self.roll_text = QtWidgets.QLabel(self.centralwidget)
        self.roll_text.setGeometry(QtCore.QRect(30, 120, 81, 16))
        self.roll_text.setObjectName("roll_text")
        self.gpscount_text = QtWidgets.QLabel(self.centralwidget)
        self.gpscount_text.setGeometry(QtCore.QRect(30, 210, 81, 16))
        self.gpscount_text.setObjectName("gpscount_text")
        self.throotle_text = QtWidgets.QLabel(self.centralwidget)
        self.throotle_text.setGeometry(QtCore.QRect(30, 180, 81, 16))
        self.throotle_text.setObjectName("throotle_text")
        self.telemetri_value = QtWidgets.QLabel(self.centralwidget)
        self.telemetri_value.setGeometry(QtCore.QRect(390, 30, 90, 16))
        self.telemetri_value.setObjectName("telemetri_value")
        self.arm_text = QtWidgets.QLabel(self.centralwidget)
        self.arm_text.setGeometry(QtCore.QRect(240, 60, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.arm_text.setFont(font)
        self.arm_text.setStyleSheet("")
        self.arm_text.setTextFormat(QtCore.Qt.AutoText)
        self.arm_text.setObjectName("arm_text")
        self.telemetri_text = QtWidgets.QLabel(self.centralwidget)
        self.telemetri_text.setGeometry(QtCore.QRect(240, 30, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.telemetri_text.setFont(font)
        self.telemetri_text.setStyleSheet("")
        self.telemetri_text.setTextFormat(QtCore.Qt.AutoText)
        self.telemetri_text.setObjectName("telemetri_text")
        self.battery_value = QtWidgets.QLabel(self.centralwidget)
        self.battery_value.setGeometry(QtCore.QRect(390, 0, 55, 16))
        self.battery_value.setObjectName("battery_value")
        self.mod_value = QtWidgets.QLabel(self.centralwidget)
        self.mod_value.setGeometry(QtCore.QRect(390, 90, 90, 16))
        self.mod_value.setStyleSheet("")
        self.mod_value.setObjectName("mod_value")
        self.mod_text = QtWidgets.QLabel(self.centralwidget)
        self.mod_text.setGeometry(QtCore.QRect(240, 90, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mod_text.setFont(font)
        self.mod_text.setStyleSheet("")
        self.mod_text.setTextFormat(QtCore.Qt.AutoText)
        self.mod_text.setObjectName("mod_text")
        self.arm_value = QtWidgets.QLabel(self.centralwidget)
        self.arm_value.setGeometry(QtCore.QRect(390, 60, 55, 16))
        self.arm_value.setObjectName("arm_value")
        self.battery_text = QtWidgets.QLabel(self.centralwidget)
        self.battery_text.setGeometry(QtCore.QRect(240, 0, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.battery_text.setFont(font)
        self.battery_text.setStyleSheet("")
        self.battery_text.setTextFormat(QtCore.Qt.AutoText)
        self.battery_text.setObjectName("battery_text")

        #tarih ve saat value burada

        self.tarih_value = QtWidgets.QLabel(self.centralwidget)
        self.tarih_value.setGeometry(QtCore.QRect(935, 10, 100,16))
        self.tarih_value.setObjectName("tarih_value")
        self.saat_value = QtWidgets.QLabel(self.centralwidget)
        self.saat_value.setGeometry(QtCore.QRect(935, 40, 100, 16))
        self.saat_value.setObjectName("saat_value")


        self.tarih_text = QtWidgets.QLabel(self.centralwidget)
        self.tarih_text.setGeometry(QtCore.QRect(890, 10, 55, 16))
        self.tarih_text.setObjectName("tarih_text")
        self.saat_text = QtWidgets.QLabel(self.centralwidget)
        self.saat_text.setGeometry(QtCore.QRect(890, 40, 55, 16))
        self.saat_text.setObjectName("saat_text")
        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1252, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_telemetry)
        self.timer.start(1000)

        self.arm_button.clicked.connect(self.armol)
        self.disarm_button.clicked.connect(self.disarm)
        self.guided_button.clicked.connect(self.guided_modu)
        self.stailize_button.clicked.connect(self.stabilize_modu)
        self.manuel_button.clicked.connect(self.manual_modu)
        self.auto_button.clicked.connect(self.auto_modu)
        self.loitter_button.clicked.connect(self.loitter_modu)
        self.rtl_button.clicked.connect(self.rtl_modu)
        self.gorev_button.clicked.connect(self.gorev_modu)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def update_telemetry(self):
        if vehicle:
            location = vehicle.location.global_relative_frame
            gps = vehicle.gps_0
            self.altitude_value.setText(f"{location.alt:.2f} m")
            self.airspeed_value.setText(f"{vehicle.airspeed:.2f} m/s")
            self.battery_value.setText(f"{vehicle.battery.voltage:.2f} V")
            self.gpsspeed_value.setText(f"{vehicle.groundspeed:.2f} m/s")
            self.distance_value.setText(f"{location.alt:.2f} m")
            self.roll_value.setText(f"{vehicle.attitude.roll:.2f}")
            self.yaw_value.setText(f"{vehicle.attitude.yaw:.2f}")
            self.gpscount_value.setText(f"{gps.satellites_visible}")
            self.throotle_value.setText(f"{vehicle.channels['3']}")
            self.telemetri_value.setText(f"{vehicle.version}")
            self.mod_value.setText(f"{vehicle.mode.name}")

        current_time = datetime.now().strftime("%H:%M:%S")
        current_date = datetime.now().strftime("%Y-%m-%d")
        self.saat_value.setText(f"{current_time}")
        self.tarih_value.setText(f"{current_date}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.arm_button.setText(_translate("MainWindow", "ARM"))
        self.disarm_button.setText(_translate("MainWindow", "DISARM"))
        self.manuel_button.setText(_translate("MainWindow", "MANUAL"))
        self.stailize_button.setText(_translate("MainWindow", "STABILIZE"))
        self.auto_button.setText(_translate("MainWindow", "AUTO"))
        self.guided_button.setText(_translate("MainWindow", "GUIDED"))
        self.loitter_button.setText(_translate("MainWindow", "LOITTER"))
        self.gorev_button.setText(_translate("MainWindow", "GOREV"))
        self.rtl_button.setText(_translate("MainWindow", "RTL"))
        self.ip_text.setText(_translate("MainWindow", "IP:"))
        self.baud_text.setText(_translate("MainWindow", "BAUD:"))
        self.altitude_value.setText(_translate("MainWindow", "TextLabel"))
        self.airspeed_value.setText(_translate("MainWindow", "TextLabel"))
        self.gpsspeed_value.setText(_translate("MainWindow", "TextLabel"))
        self.distance_value.setText(_translate("MainWindow", "TextLabel"))
        self.throotle_value.setText(_translate("MainWindow", "TextLabel"))
        self.roll_value.setText(_translate("MainWindow", "TextLabel"))
        self.yaw_value.setText(_translate("MainWindow", "TextLabel"))
        self.gpscount_value.setText(_translate("MainWindow", "TextLabel"))
        self.gpsspeed_text.setText(_translate("MainWindow", "GPS HIZI:"))
        self.yaw_text.setText(_translate("MainWindow", "YAW:"))
        self.altitude_text.setText(_translate("MainWindow", "YÜKSEKLİK:"))
        self.airspeed_text.setText(_translate("MainWindow", "HAVA HIZI:"))
        self.distance_text.setText(_translate("MainWindow", "UZAKLIK:"))
        self.roll_text.setText(_translate("MainWindow", "ROLL:"))
        self.battery_value.setText(_translate("MainWindow", "ğ"))
        self.gpscount_text.setText(_translate("MainWindow", "GPS SAYISI:"))
        self.throotle_text.setText(_translate("MainWindow", "GAZ:"))
        self.telemetri_value.setText(_translate("MainWindow", "TextLabel"))
        self.arm_text.setText(_translate("MainWindow", "ARM:"))
        self.telemetri_text.setText(_translate("MainWindow", "TELEMETRİ:"))

        self.mod_value.setText(_translate("MainWindow", "TextLabel"))
        self.mod_text.setText(_translate("MainWindow", "MOD:"))
        self.arm_value.setText(_translate("MainWindow", "TextLabel"))
        self.battery_text.setText(_translate("MainWindow", "BATARYA:"))
        self.tarih_value.setText(_translate("MainWindow", "TextLabel"))
        self.saat_value.setText(_translate("MainWindow", "TextLabel"))
        self.tarih_text.setText(_translate("MainWindow", "TARİH:"))
        self.saat_text.setText(_translate("MainWindow", "SAAT:"))


#hava aracına ip ile bağlanma
    class DroneConnection:
        def __init__(self, ip_value, baudrate=123):
            self.ip_value = ip_value
            self.baudrate = baudrate
            self.vehicle = None

        def connect_drone(self):
            try:

                connection_string = f'{self.ip_value}:{self.baudrate}'
                self.vehicle = connect(connection_string, wait_ready=True)
                print(f"Bağlantı başarılı! IP: {self.ip_value}, Baudrate: {self.baudrate}")
            except Exception as e:
                print(f"Bağlantı hatası: {str(e)}")

        def disconnect_drone(self):
            if self.vehicle:
                self.vehicle.close()
                print("Bağlantı kapatıldı.")
            else:
                print("Bağlantı zaten kapalı.")



    def armol(self):

        while vehicle.is_armable == False:
            print("ARAÇ HAZIR DEĞİL")
            time.sleep(1)
        if vehicle.is_armable == True:

            vehicle.armed = True
            print("ARM EDİLDİ")

            if vehicle.armed == True:
                print("ARAÇ ZATEN ARM EDİLDİ")



    def disarm(self):

        vehicle.armed = False
        print("DİSARMED EDİLDİ")

    def guided_modu(self):

        vehicle.mode = VehicleMode("GUIDED")
        print("GUIDED")

    def stabilize_modu(self):

        vehicle.mode = VehicleMode("STABILIZE")
        print("STABILIZE")

    def manual_modu(self):

        vehicle.mode = VehicleMode("MANUAL")
        print("MANUAL")

    def auto_modu(self):

        vehicle.mode = VehicleMode("AUTO")
        print("AUTO")

    def loitter_modu(self):

        vehicle.mode = VehicleMode("LOITTER")
        print("LOITTER")

    def rtl_modu(self):

        vehicle.mode = VehicleMode("RTL")
        print("RTL")

    def gorev_modu(self):

        vehicle.mode = VehicleMode("GOREV")
        print("GOREV")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
