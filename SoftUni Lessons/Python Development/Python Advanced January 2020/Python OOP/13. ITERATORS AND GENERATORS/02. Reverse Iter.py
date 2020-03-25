# Done in class!


class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = len(self.iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value_to_return = self.iterable[self.index]
        self.index -= 1
        return value_to_return
