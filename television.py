


class Television():
    MIN_VOLUME = 0
    MAX_VOLUME = 0
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL


    def power(self):
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self):
        if self.__muted == False:
            self.__muted = True
        else:
            self.__muted = False
    
    def channel_up(self):
        chan = (self.__channel + 1)%(Television.MAX_CHANNEL+1)
        self.__channel = chan

    def channel_down(self):
        chan = (self.__channel - 1)%(Television.MAX_CHANNEL+1)
        self.__channel = chan


    def volume_up(self):
        if self.__muted == True:
            self.__muted = False
        self.__volume = (self.__volume + 1)%(Television.MAX_VOLUME+1)

    def volume_down(self):
        if self.__muted == True:
            self.__muted = False
        self.__volume = (self.__volume - 1)%(Television.MAX_VOLUME+1)

    def __str__(self):
        return f"Power: {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"


        


