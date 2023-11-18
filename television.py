


class Television():
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 0
    MIN_CHANNEL: int = 0
    MAX_CHANNE: int = 3
    def __init__(self) -> None:
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL


    def power(self) -> None:
        """Turns TV ON or OFF based of __status variable. Returns non"""
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """Mutes or unmutes the TV based on __muted variable. Returns none"""
        if self.__muted == False:
            self.__muted = True
        else:
            self.__muted = False
    
    def channel_up(self) -> None:
        """Changes the channel up. Returns none"""
        chan = (self.__channel + 1)%(Television.MAX_CHANNEL+1)
        self.__channel = chan

    def channel_down(self) -> None:
        """Changest the channel down. Returns none"""
        chan = (self.__channel - 1)%(Television.MAX_CHANNEL+1)
        self.__channel = chan


    def volume_up(self) -> None:
        """Turns the volume up 1. Returns none"""
        if self.__muted == True:
            self.__muted = False
        self.__volume = (self.__volume + 1)%(Television.MAX_VOLUME+1)

    def volume_down(self) -> None:
        """Turns the volume down 1. Returns none"""
        self.__volume = (self.__volume - 1)%(Television.MAX_VOLUME+1)

    def __str__(self) -> None:
        """Generates the string when running print(class). Returns str"""
        return f"Power: {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"


        


