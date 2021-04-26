# 일반적인 운송수단을 나타내는 클래스이다.
class Vehicle:
    def __init__(self,make,model,color,price):
            self.make = make
            self.model = model
            self.color = color
            self.price = price
            
def setMake(self, make): # 설정자 메소드
    self.make = make
def getMake(self): # 접근자 메소드
    return self.make
    
    # 차량에 대한 정보를 문자열로 요약하여서 반환한다.
    def getDesc(self):
        return "차량 =("+str(self.make)+","+\
            str(self.model)+","+\
            str(self.color)+","+\
            str(self.price)+")"
    
class Truck(Vehicle) :
    def __init__(self, make, model, color, price, payload):
      super().__init__(make, model, color, price)
      self.payload=payload

    def setPayload(self, paylad):
        self.payload=payload
    def getPayload(self): # 접근자 메소드
        return self.payload
    
    def main(): # main() 함수 정의
        myTruck = Truck("Tisla", "Model S", "white", 10000, 2000)
        myTruck.setMake("Tesla") # 설정자 메소드 호출
        myTruck.setPayload(2000) # 설정자 메소드 호출
        print(myTruck.getDesc()) # 트럭 객체를 문자열로 출력