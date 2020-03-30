class CustomList:
    def __init__(self, *args):
        """It can initiate object with attribute data[list].
        If no arguments are given they are added to the data."""
        self.data = [item for item in args]

    def append(self, value):
        """ Adds a value to the end of the list. Returns the list."""
        self.data += [value]
        return self.data

    def remove(self, index):
        """Removes the value on the index. Returns the value removed."""
        return self.data.pop(index)

    def get(self, index):
        """Returns the value on the index."""
        return self.data[index]

    def extend(self, iterable):
        """Appends the iterable to the list. Returns the new list."""
        self.data = [self.data.append(element) for element in iterable]
        return self.data

    def insert(self, index, value):
        """Adds the value on the specific index. Returns the list."""
        self.data = self.data[:index] + [value] + self.data[index:]
        return self.data

    def pop(self):
        """Removes the last value and returns it."""
        return self.data.pop()

    def clear(self):
        """Removes all values, contained in the list."""
        self.data = []

    def index(self, value):
        """Returns the index of the given value"""
        return self.data.index(value)

    def count(self, value):
        """Returns the number of times the value is contained in the list."""
        return self.data.count(value)

    def reverse(self):
        """Returns the values of the list in reverse order."""
        return self.data[::-1]

    def copy(self):
        """Returns a copy of the list."""
        return self.data.copy()

    # Advanced Functions:
    def size(self):
        """Returns the length of the list."""
        return len(self.data)

    def add_first(self, value):
        """Adds the value at the beginning of the list"""
        self.data.insert(0, value)

    def dictionize(self):
        """Adds the value at the beginning of the list
        dictionize() – Returns the list as a dictionary:
        The keys will be each value on an even position
        and their values will be each value on an odd position.
        If the last value on an even position,
        it’s value will be " " (space)
        """
        dictionary = {}
        for item in range(0, len(self.data), 2):
            if item % 2 == 0:
                if (item + 1) < len(self.data):
                    dictionary[self.data[item]] = self.data[item + 1]
                else:
                    dictionary[self.data[item]] = ' '
                    break
        return dictionary

    def move(self, amount):
        """Move the first "amount" of values to the end of the list. Returns the list."""
        self.data = self.data[amount:] + self.data[:amount]
        return self.data

    def sum(self):
        """Returns the sum of the list.
        If the value is not a number, add the length of the value to the overall number."""
        total = 0
        for item in self.data:
            if (type(item) == int) or (type(item) == float):
                total += item
            else:
                total += len(item)
        return total

    def overbound(self):
        """Returns the index of the biggest value. If the value is not a number, check it’s length."""
        biggest = -100000000000
        index = 0
        for item in range(len(self.data)):
            if (type(self.data[item]) == int) or (type(self.data[item]) == float):
                if self.data[item] >= biggest:
                    biggest = self.data[item]
                    index = item
            else:
                if len(self.data[item]) >= biggest:
                    biggest = len(self.data[item])
                    index = item
        return index

    def underbound(self):
        """Returns the index of the smallest value. If the value is not a number, check it’s length."""
        smallest = 100000000000
        index = 0
        for item in range(len(self.data)):
            if (type(self.data[item]) == int) or (type(self.data[item]) == float):
                if self.data[item] <= smallest:
                    smallest = self.data[item]
                    index = item
            else:
                if len(self.data[item]) <= smallest:
                    smallest = len(self.data[item])
                    index = item
        return index
