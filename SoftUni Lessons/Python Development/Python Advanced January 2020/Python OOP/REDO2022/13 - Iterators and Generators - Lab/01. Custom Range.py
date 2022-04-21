class custom_range:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.index = first

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.last:
            raise StopIteration
        index = self.index
        self.index += 1
        return index
