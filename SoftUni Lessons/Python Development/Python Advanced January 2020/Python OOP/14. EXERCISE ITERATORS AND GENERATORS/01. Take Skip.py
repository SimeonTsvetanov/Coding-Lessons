class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        current = self.current
        self.current += self.step
        self.counter += 1
        if self.counter > self.count:
            raise StopIteration
        return current


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
