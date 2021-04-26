class Vehicle:
    def __init__(self,name):
        self.name = name
    def drive(Vehicle):
        return '알 수 없음'
    
        
class truck(Vehicle):
    def drive(self):
        return '트럭을 운전합니다.'
    
class car(Vehicle):
    def drive(self):
        return '승용차를 운전합니다.'


carList = [truck('truck1'),
        truck('truck2'),
        car('car1')]

for a in carList:
    print (a.name + ': ' + a.drive())
