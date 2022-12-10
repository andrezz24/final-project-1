class Television:
    """
    Class that represents a Television object
    """
    MIN_VOLUME = 0
    MAX_VOlUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 6

    def __init__(self) -> None:
        """
        Constructor to create initial state of TV object.
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method that changes the current TV status
        """
        if self.__status is False:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """
        Method that will mute the TV.
        """
        if self.__muted is False:
            self.__muted = True

        else:
            self.__muted = False

    def channel_up(self) -> None:
        """
        Method that increases the TV channel by 1.
        """
        if self.__status is True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        """
        Method that decreases the TV channel by 1.
        """
        if self.__status is True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        """
        Method that increases the TV volume by 1.
        """
        if self.__status is True:
            if self.__volume == Television.MAX_VOlUME:
                pass
            elif self.__muted is True:
                self.__muted = False
                self.__volume += 1
            else:
                self.__volume += 1

    def volume_down(self):
        """
        Method that decreases the TV volume by 1.
        """
        if self.__status is True:
            if self.__volume == Television.MIN_VOLUME:
                pass
            elif self.__muted is True:
                self.__muted = False
                self.__volume -= 1
            else:
                self.__volume -= 1

    def get_status(self) -> bool:
        """
        Method that gets the current TV status
        :return: True or False depending on TV status
        """
        return self.__status

    def get_channel(self) -> int:
        """
        Method that gets the current TV channel.
        :return: TV channel as int value
        """
        return int(self.__channel)

    def get_volume(self) -> int:
        """
        Method that gets the current TV volume.
        :return: TV volume as int value
        """
        return int(self.__volume)

    def set_volume(self, vol: int):
        """
        Method that sets the TV Volume
        :param vol: TV volume chose by user.
        """
        self.__volume = vol

    def set_channel(self, ch):
        """
        Method that sets the TV channel.
        :param ch: TV channel chose by user.
        """
        self.__channel = ch

    def __str__(self):
        if self.__muted is False:
            return f'TV status: Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        else:
            return f'TV status: Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
