from lab import Television
from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

tv_1 = Television()  # creates the TV object


class Controller(QMainWindow, Ui_MainWindow):
    """
    A class to represent the controller and link the GUI with the 'lab' module.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.pushButton_power.clicked.connect(lambda: self.power_button())
        self.pushButton_channel_up.clicked.connect(lambda: self.channel_button_up())
        self.pushButton_channel_down.clicked.connect(lambda: self.channel_down_button())
        self.pushButton_ch0.clicked.connect(lambda: self.set_ch0())
        self.pushButton_ch1.clicked.connect(lambda: self.set_ch1())
        self.pushButton_ch2.clicked.connect(lambda: self.set_ch2())
        self.pushButton_ch3.clicked.connect(lambda: self.set_ch3())
        self.pushButton_ch4.clicked.connect(lambda: self.set_ch4())
        self.pushButton_ch5.clicked.connect(lambda: self.set_ch5())
        self.pushButton_ch6.clicked.connect(lambda: self.set_ch6())
        self.pushButton_volume_up.clicked.connect(lambda: self.volume_button_up())
        self.pushButton_volume_down.clicked.connect(lambda: self.volume_down_button())
        self.pushButton_mute.clicked.connect(lambda: self.mute_volume())

    def power_button(self) -> None:
        """
        This method links the power button with the power method from the module 'lab'
        Method also changes the TV channel picture displayed on remote
        """
        tv_1.power()
        print(tv_1)
        if tv_1.get_status() is True:
            self.pushButton_power.setText('ON')

            if tv_1.get_channel() == 0:
                self.label_for_image.setPixmap(QtGui.QPixmap("images/espn.jpeg"))
            elif tv_1.get_channel() == 1:
                self.label_for_image.setPixmap(QtGui.QPixmap("images/cnn.png"))
            elif tv_1.get_channel() == 2:
                self.label_for_image.setPixmap(QtGui.QPixmap("images/fox.jpeg"))
            elif tv_1.get_channel() == 3:
                self.label_for_image.setPixmap(QtGui.QPixmap("images/nbc.jpeg"))
            elif tv_1.get_channel() == 4:
                self.label_for_image.setPixmap(QtGui.QPixmap("images/cbs.jpeg"))
            elif tv_1.get_channel() == 5:
                self.label_for_image.setPixmap(QtGui.QPixmap("images/nfl-redzone.jpg"))
            else:
                self.label_for_image.setPixmap(QtGui.QPixmap("images/abc.png"))
        else:
            self.pushButton_power.setText('OFF')
            self.label_for_image.setPixmap(QtGui.QPixmap("images/blackscreen.jpeg"))

    def channel_button_up(self) -> None:
        """
        Method that links channel up button on gui to 'channel_up' method from 'lab' module.
        Method also changes the TV channel picture displayed on remote whenever this button is clicked.
        """
        if tv_1.get_status() is True:
            tv_1.channel_up()
            self.verticalSlider_ch.setSliderPosition(tv_1.get_channel())

            if tv_1.get_channel() == 0:
                self.label_for_image.setPixmap(QtGui.QPixmap("images/espn.jpeg"))
            elif tv_1.get_channel() == 1:
                self.label_for_image.setPixmap(QtGui.QPixmap("images/cnn.png"))
            elif tv_1.get_channel() == 2:
                self.label_for_image.setPixmap(QtGui.QPixmap("images/fox.jpeg"))
            elif tv_1.get_channel() == 3:
                self.label_for_image.setPixmap(QtGui.QPixmap("images/nbc.jpeg"))
            elif tv_1.get_channel() == 4:
                self.label_for_image.setPixmap(QtGui.QPixmap("images/cbs.jpeg"))
            elif tv_1.get_channel() == 5:
                self.label_for_image.setPixmap(QtGui.QPixmap("images/nfl-redzone.jpg"))
            else:
                self.label_for_image.setPixmap(QtGui.QPixmap("images/abc.png"))
            print(tv_1)

    def channel_down_button(self) -> None:
        """
        Method links the channel down button with 'channel_down' method from 'lab' module.
        Method also changes the TV Channel picture displayed on remote whenever this button is clicked.
        """
        if tv_1.get_status() is True:
            tv_1.channel_down()
            self.verticalSlider_ch.setSliderPosition(tv_1.get_channel())

            if tv_1.get_channel() == 0:
                self.label_for_image.setPixmap(QtGui.QPixmap("images/espn.jpeg"))
            elif tv_1.get_channel() == 1:
                self.label_for_image.setPixmap(QtGui.QPixmap("images/cnn.png"))
            elif tv_1.get_channel() == 2:
                self.label_for_image.setPixmap(QtGui.QPixmap("images/fox.jpeg"))
            elif tv_1.get_channel() == 3:
                self.label_for_image.setPixmap(QtGui.QPixmap("images/nbc.jpeg"))
            elif tv_1.get_channel() == 4:
                self.label_for_image.setPixmap(QtGui.QPixmap("images/cbs.jpeg"))
            elif tv_1.get_channel() == 5:
                self.label_for_image.setPixmap(QtGui.QPixmap("images/nfl-redzone.jpg"))
            else:
                self.label_for_image.setPixmap(QtGui.QPixmap("images/abc.png"))
            print(tv_1)

    def volume_button_up(self) -> None:
        """
        Method that links the volume up button from gui to 'volume_up' method from 'lab' module.
        Method also changes the volume slider up when volume up button is clicked.
        """
        if tv_1.get_status() is True:
            tv_1.volume_up()
            self.verticalSlider_vol.setSliderPosition(tv_1.get_volume())
            print(tv_1)

    def volume_down_button(self) -> None:
        """
        Method that links the volume down button on gui to method from 'lab' module.
        Method also changes the volume slider down when volume down button is clicked.
        """
        if tv_1.get_status() is True:
            tv_1.volume_down()
            self.verticalSlider_vol.setSliderPosition(tv_1.get_volume())
            print(tv_1)

    def mute_volume(self) -> None:
        """
        This method calls on the mute function from lab.py and mutes the TV volume
        """
        if tv_1.get_status() is True:
            tv_1.mute()
            print(tv_1)
            if self.verticalSlider_vol.value() != 0:
                self.verticalSlider_vol.setSliderPosition(0)
            else:
                self.verticalSlider_vol.setSliderPosition(tv_1.get_volume())

    def set_ch0(self) -> None:
        """
        Method links the '6' button on remote to setter from 'lab' module.
        """
        if tv_1.get_status() is True:
            tv_1.set_channel(0)
            self.verticalSlider_ch.setSliderPosition(tv_1.get_channel())
            self.label_for_image.setPixmap(QtGui.QPixmap("images/espn.jpeg"))
            print(tv_1)

    def set_ch1(self) -> None:
        """
        Method links the '6' button on remote to setter from 'lab' module.
        """
        if tv_1.get_status() is True:
            tv_1.set_channel(1)
            self.verticalSlider_ch.setSliderPosition(tv_1.get_channel())
            self.label_for_image.setPixmap(QtGui.QPixmap("images/cnn.png"))
            print(tv_1)

    def set_ch2(self) -> None:
        """
        Method links the '2' button on remote to setter from 'lab' module.
        """
        if tv_1.get_status() is True:
            tv_1.set_channel(2)
            self.verticalSlider_ch.setSliderPosition(tv_1.get_channel())
            self.label_for_image.setPixmap(QtGui.QPixmap("images/fox.jpeg"))
            print(tv_1)

    def set_ch3(self) -> None:
        """
        Method links the '3' button on remote to setter from 'lab' module.
        """
        if tv_1.get_status() is True:
            tv_1.set_channel(3)
            self.verticalSlider_ch.setSliderPosition(tv_1.get_channel())
            self.label_for_image.setPixmap(QtGui.QPixmap("images/nbc.jpeg"))
            print(tv_1)

    def set_ch4(self) -> None:
        """
        Method links the '4' button on remote to setter from 'lab' module.
        """
        if tv_1.get_status() is True:
            tv_1.set_channel(4)
            self.verticalSlider_ch.setSliderPosition(tv_1.get_channel())
            self.label_for_image.setPixmap(QtGui.QPixmap("images/cbs.jpeg"))
            print(tv_1)

    def set_ch5(self) -> None:
        """
        Method links the '5' button on remote to setter from 'lab' module.
        """
        if tv_1.get_status() is True:
            tv_1.set_channel(5)
            self.verticalSlider_ch.setSliderPosition(tv_1.get_channel())
            self.label_for_image.setPixmap(QtGui.QPixmap("images/nfl-redzone.jpg"))
            print(tv_1)

    def set_ch6(self) -> None:
        """
        Method links the '6' button on remote to setter from 'lab' module.
        """
        if tv_1.get_status() is True:
            tv_1.set_channel(6)
            self.verticalSlider_ch.setSliderPosition(tv_1.get_channel())
            self.label_for_image.setPixmap(QtGui.QPixmap("images/abc.png"))
            print(tv_1)
