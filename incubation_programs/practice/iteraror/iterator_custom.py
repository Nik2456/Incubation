class CountDown:
    
    def __init__(self,start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start<=0:
            raise StopIteration
        value = self.start
        self.start -= 1
        return value

for num in CountDown(10):
    print(num)
