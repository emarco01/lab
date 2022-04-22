class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        """
        - Create a private variable to store the TV channel. It should be set to the minimum TV channel by default.
        - Create a private variable to store the TV volume. It should be set to the minimum TV volume by default.
        - Create a private variable to store the TV status. The TV should start when it is off.
        """
        self.__TV_channel = self.MIN_CHANNEL
        self.__TV_volume = self.MIN_VOLUME
        self.__TV_status = False

    def power(self):
        """
        - This method should be used to turn the TV on/off.
        - If called on a TV object that is off, the TV object should be turned on.
        - If called on a TV object that is on, the TV object should be turned off.
        """
        if self.__TV_status is False:
            self.__TV_status = True
        elif self.__TV_status is True:
            self.__TV_status = False

    def channel_up(self):
        """
        - This method should be used to adjust the TV channel by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_CHANNEL, it should take the TV channel back to the MIN_CHANNEL.
        """
        if self.__TV_status is True:
            if self.__TV_channel < self.MAX_CHANNEL:
                self.__TV_channel += 1
            elif self.__TV_channel == self.MAX_CHANNEL:
                self.__TV_channel = self.MIN_CHANNEL

    def channel_down(self):
        """
        - This method should be used to adjust the TV channel by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_CHANNEL, it should take the TV channel back to the MAX_CHANNEL.
        """
        if self.__TV_status is True:
            if self.__TV_channel > self.MIN_CHANNEL:
                self.__TV_channel -= 1
            elif self.__TV_channel == self.MIN_CHANNEL:
                self.__TV_channel = self.MAX_CHANNEL

    def volume_up(self):
        """
        - This method should be used to adjust the TV volume by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_VOLUME, the volume should not be adjusted.
        """
        if self.__TV_status is True:
            if self.__TV_volume < self.MAX_VOLUME:
                self.__TV_volume += 1

    def volume_down(self):
        """
        - This method should be used to adjust the TV volume by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_VOLUME, the volume should not be adjusted.
        """
        if self.__TV_status is True:
            if self.__TV_volume > self.MIN_VOLUME:
                self.__TV_volume -= 1

    def __str__(self):
        """
        - This method should be used to return the TV status using the format shown in the comments of main.py
        """
        return f'TV Status: Is on = {self.__TV_status}, Channel = {self.__TV_channel}, Volume = {self.__TV_volume}'
