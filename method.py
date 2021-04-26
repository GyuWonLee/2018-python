class Television:
    def __init__(self, channel, volume, on):
        self.__channel = channel
        self.__volume = volume
        self.__on = on
        
    def show(self):
        print(self.__channel, self.__volume, self.__con)
    
    def setChannel(self, channel):
        self.channel = channel
        
    def getChannel(self):
        if self.__on:
            return self.channel
    def volumeUp(self):
        if self.on:
            self.__volume += 1
    def volumeDown(self):
        if self.__on:
            self.__volume -= 1
    def onOff(self):
        self.__on = not self.on

t = Television(9, 10, True)

t.show()
t.setChannel(11)
t.show()
    