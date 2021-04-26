class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        print("계산할 수 없음!")
    def perimeter(self):
        print("계산할 수 없음!")
    
class Rectangle(Shape):
    def __init__(self,x,y,w,h):
        super().__init__(x, y)
        self.w = w
        self.h = h
        
    def area(self):
        return self.w*self.h
    def perimeter(self):
        return 2*(self.w+self.h)
    
def Square(Shape):
    def __init__(self,x,y,w):
        super().__init__(x, y)
        self.w = w
    def area(self):
        return self.w**2
    def perimeter(self):
        return 4*self.w
     
    

r = Rectangle(0, 0, 100, 200)
print("사각형의 면적",r.area())
print("사각형의 둘레",r.perimeter())

s = Square(0, 0, 100)
print("정사각형의 면적 : ",s.area())
print("정사각형의 둘레 : ",s.perimeter())