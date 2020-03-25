class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.idx = self.count

    def __iter__(self):
        return self

    def __next__(self):
        index = self.idx
        if index < 0:
            raise StopIteration
        self.idx -= 1
        return index


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
