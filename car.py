class car:
    def __init__(self, speed = 0, gear = 1, color = "pink"):
        self.__speed = speed
        self.__gear = gear
        self.__color = color
        
    def serSpeed(self):
        if self.__speed < 300:
            self.__speed += 10;
        
        if self.__speed > 1:
            self.__speed -= 1;
            
    def setGear(self, gear):
        self.__gear = gear;
    
    def setColor(self, color):
        self.__color = color;
        
    #def __str__(self):
     #   return '(%d, %d, %s)' % (self.__speed, self.__gear, self.__color)
    
myCar = car()
myCar.setGear(3);
myCar.setColor(100);
print(myCar)

