class Television:
    serialNumber = 0 # 이것이 정적 변수이다.
    def __init__(self):
        Television.serialNumber += 1
        self.number = Television.serialNumber


t1 = Television()
t2 = Television()
t3 = Television()