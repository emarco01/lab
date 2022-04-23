class Television:
    """
    Class that represents the TV objects.
    """
    MIN_CHANNEL: int = 0     # Minimum TV channel
    MAX_CHANNEL: int = 3     # Maximum TV channel

    MIN_VOLUME: int = 0      # Minimum TV volume
    MAX_VOLUME: int = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Method to set the default parameters of the TV.
        """
        self.__TV_channel: int = self.MIN_CHANNEL
        self.__TV_volume: int = self.MIN_VOLUME
        self.__TV_status: bool = False

    def power(self) -> None:
        """
        Method to change the TV between on and off.
        """
        if self.__TV_status is False:
            self.__TV_status = True
        elif self.__TV_status is True:
            self.__TV_status = False

    def channel_up(self) -> None:
        """
        Method that changes the channel number up.
            Should only work if the TV is on.
            If __TV_channel is at the value of MAX_CHANNEL, then the channel should go to MIN_CHANNEL.
        """
        if self.__TV_status is True:
            if self.__TV_channel < self.MAX_CHANNEL:
                self.__TV_channel += 1
            elif self.__TV_channel == self.MAX_CHANNEL:
                self.__TV_channel = self.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method that changes the channel number down.
            Should only work if the TV is on.
            If __TV_channel is at the value of MIN_CHANNEL, then the channel should go to MAX_CHANNEL.
        """
        if self.__TV_status is True:
            if self.__TV_channel > self.MIN_CHANNEL:
                self.__TV_channel -= 1
            elif self.__TV_channel == self.MIN_CHANNEL:
                self.__TV_channel = self.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method that increases the volume by 1.
            Should only work if the TV is on.
            If __TV_volume is at the value of MAX_VOLUME, then the volume should not change.
        """
        if self.__TV_status is True:
            if self.__TV_volume < self.MAX_VOLUME:
                self.__TV_volume += 1

    def volume_down(self) -> None:
        """
        Method that increases the volume by 1.
            Should only work if the TV is on.
            If __TV_volume is at the value of MIN_VOLUME, then the volume should not change.
        """
        if self.__TV_status is True:
            if self.__TV_volume > self.MIN_VOLUME:
                self.__TV_volume -= 1

    def __str__(self) -> str:
        """
        Method that returns the status of the TV.
        :return: String with the TV status: The power state, Channel, and Volume.
        """
        return f'TV Status: Is on = {self.__TV_status}, Channel = {self.__TV_channel}, Volume = {self.__TV_volume}'
