# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newtvremote.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 750)
        MainWindow.setMinimumSize(QtCore.QSize(450, 750))
        MainWindow.setMaximumSize(QtCore.QSize(450, 750))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalSlider_vol = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_vol.setGeometry(QtCore.QRect(410, 60, 22, 160))
        self.verticalSlider_vol.setMaximum(2)
        self.verticalSlider_vol.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_vol.setTickInterval(1)
        self.verticalSlider_vol.setObjectName("verticalSlider_vol")
        self.label_for_image = QtWidgets.QLabel(self.centralwidget)
        self.label_for_image.setGeometry(QtCore.QRect(60, 60, 321, 161))
        self.label_for_image.setText("")
        self.label_for_image.setPixmap(QtGui.QPixmap("../../Downloads/blackscreen.jpeg"))
        self.label_for_image.setScaledContents(True)
        self.label_for_image.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_for_image.setObjectName("label_for_image")
        self.pushButton_channel_up = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_channel_up.setGeometry(QtCore.QRect(50, 270, 61, 91))
        self.pushButton_channel_up.setObjectName("pushButton_channel_up")
        self.pushButton_channel_down = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_channel_down.setGeometry(QtCore.QRect(50, 360, 61, 91))
        self.pushButton_channel_down.setObjectName("pushButton_channel_down")
        self.pushButton_volume_down = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_volume_down.setGeometry(QtCore.QRect(330, 360, 61, 91))
        self.pushButton_volume_down.setObjectName("pushButton_volume_down")
        self.pushButton_volume_up = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_volume_up.setGeometry(QtCore.QRect(330, 270, 61, 91))
        self.pushButton_volume_up.setObjectName("pushButton_volume_up")
        self.pushButton_mute = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mute.setGeometry(QtCore.QRect(170, 341, 100, 41))
        self.pushButton_mute.setObjectName("pushButton_mute")
        self.pushButton_ch1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ch1.setGeometry(QtCore.QRect(110, 460, 61, 71))
        self.pushButton_ch1.setObjectName("pushButton_ch1")
        self.pushButton_ch2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ch2.setGeometry(QtCore.QRect(190, 460, 61, 71))
        self.pushButton_ch2.setObjectName("pushButton_ch2")
        self.pushButton_ch3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ch3.setGeometry(QtCore.QRect(270, 460, 61, 71))
        self.pushButton_ch3.setObjectName("pushButton_ch3")
        self.pushButton_ch6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ch6.setGeometry(QtCore.QRect(270, 530, 61, 71))
        self.pushButton_ch6.setObjectName("pushButton_ch6")
        self.pushButton_ch4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ch4.setGeometry(QtCore.QRect(110, 530, 61, 71))
        self.pushButton_ch4.setObjectName("pushButton_ch4")
        self.pushButton_ch5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ch5.setGeometry(QtCore.QRect(190, 530, 61, 71))
        self.pushButton_ch5.setObjectName("pushButton_ch5")
        self.pushButton_ch0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ch0.setGeometry(QtCore.QRect(190, 600, 61, 71))
        self.pushButton_ch0.setObjectName("pushButton_ch0")
        self.pushButton_power = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_power.setGeometry(QtCore.QRect(310, 10, 100, 32))
        self.pushButton_power.setObjectName("pushButton_power")
        self.label_channel = QtWidgets.QLabel(self.centralwidget)
        self.label_channel.setGeometry(QtCore.QRect(50, 240, 58, 16))
        self.label_channel.setAlignment(QtCore.Qt.AlignCenter)
        self.label_channel.setObjectName("label_channel")
        self.label_volume = QtWidgets.QLabel(self.centralwidget)
        self.label_volume.setGeometry(QtCore.QRect(330, 240, 58, 16))
        self.label_volume.setAlignment(QtCore.Qt.AlignCenter)
        self.label_volume.setObjectName("label_volume")
        self.verticalSlider_ch = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_ch.setGeometry(QtCore.QRect(10, 60, 22, 160))
        self.verticalSlider_ch.setMaximum(6)
        self.verticalSlider_ch.setPageStep(0)
        self.verticalSlider_ch.setSliderPosition(0)
        self.verticalSlider_ch.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_ch.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider_ch.setTickInterval(0)
        self.verticalSlider_ch.setObjectName("verticalSlider_ch")
        self.label_ch0 = QtWidgets.QLabel(self.centralwidget)
        self.label_ch0.setGeometry(QtCore.QRect(40, 201, 20, 20))
        self.label_ch0.setObjectName("label_ch0")
        self.label_ch1 = QtWidgets.QLabel(self.centralwidget)
        self.label_ch1.setGeometry(QtCore.QRect(40, 179, 20, 16))
        self.label_ch1.setObjectName("label_ch1")
        self.label_ch2 = QtWidgets.QLabel(self.centralwidget)
        self.label_ch2.setGeometry(QtCore.QRect(40, 151, 20, 20))
        self.label_ch2.setObjectName("label_ch2")
        self.label_ch3 = QtWidgets.QLabel(self.centralwidget)
        self.label_ch3.setGeometry(QtCore.QRect(40, 130, 20, 16))
        self.label_ch3.setObjectName("label_ch3")
        self.label_ch4 = QtWidgets.QLabel(self.centralwidget)
        self.label_ch4.setGeometry(QtCore.QRect(40, 101, 20, 20))
        self.label_ch4.setObjectName("label_ch4")
        self.label_ch5 = QtWidgets.QLabel(self.centralwidget)
        self.label_ch5.setGeometry(QtCore.QRect(40, 75, 20, 21))
        self.label_ch5.setObjectName("label_ch5")
        self.label_ch6 = QtWidgets.QLabel(self.centralwidget)
        self.label_ch6.setGeometry(QtCore.QRect(40, 50, 16, 16))
        self.label_ch6.setObjectName("label_ch6")
        self.label_vol0 = QtWidgets.QLabel(self.centralwidget)
        self.label_vol0.setGeometry(QtCore.QRect(390, 200, 16, 16))
        self.label_vol0.setObjectName("label_vol0")
        self.label_vol1 = QtWidgets.QLabel(self.centralwidget)
        self.label_vol1.setGeometry(QtCore.QRect(390, 130, 16, 16))
        self.label_vol1.setObjectName("label_vol1")
        self.label_ch2_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_ch2_2.setGeometry(QtCore.QRect(390, 60, 16, 16))
        self.label_ch2_2.setObjectName("label_ch2_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TV Remote"))
        self.pushButton_channel_up.setText(_translate("MainWindow", "+"))
        self.pushButton_channel_down.setText(_translate("MainWindow", "-"))
        self.pushButton_volume_down.setText(_translate("MainWindow", "-"))
        self.pushButton_volume_up.setText(_translate("MainWindow", "+"))
        self.pushButton_mute.setText(_translate("MainWindow", "MUTE"))
        self.pushButton_ch1.setText(_translate("MainWindow", "1"))
        self.pushButton_ch2.setText(_translate("MainWindow", "2"))
        self.pushButton_ch3.setText(_translate("MainWindow", "3"))
        self.pushButton_ch6.setText(_translate("MainWindow", "6"))
        self.pushButton_ch4.setText(_translate("MainWindow", "4"))
        self.pushButton_ch5.setText(_translate("MainWindow", "5"))
        self.pushButton_ch0.setText(_translate("MainWindow", "0"))
        self.pushButton_power.setText(_translate("MainWindow", "OFF"))
        self.label_channel.setText(_translate("MainWindow", "Channel"))
        self.label_volume.setText(_translate("MainWindow", "Volume"))
        self.label_ch0.setText(_translate("MainWindow", "0"))
        self.label_ch1.setText(_translate("MainWindow", "1"))
        self.label_ch2.setText(_translate("MainWindow", "2"))
        self.label_ch3.setText(_translate("MainWindow", "3"))
        self.label_ch4.setText(_translate("MainWindow", "4"))
        self.label_ch5.setText(_translate("MainWindow", "5"))
        self.label_ch6.setText(_translate("MainWindow", "6"))
        self.label_vol0.setText(_translate("MainWindow", "0"))
        self.label_vol1.setText(_translate("MainWindow", "1"))
        self.label_ch2_2.setText(_translate("MainWindow", "2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
