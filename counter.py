class Counter:
    def reset(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def get(self):
        return self.count
    

c1 = Counter()
c1.reset()
c1.increment()
c1.__count = 10000
print(c1.get())