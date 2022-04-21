class reverse_iter:
    def __init__(self, items):
        self.items = items
        self.index = len(self.items)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        index = self.index
        self.index -= 1
        return self.items[self.index]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
