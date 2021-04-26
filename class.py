class Counter:
    def reset(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def get(self):
        return self.count
    
a = Counter()
a.reset()
a.increment()
a.increment()

print("카운터 a의 값은", a.get())


b = Counter()
b.reset()
b.increment()
b.increment()
b.increment()

print("카운터 b의 값은", b.get())

