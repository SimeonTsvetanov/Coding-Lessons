class vowels:
    def __init__(self, string):
        self.string = [le for le in string if le.lower() in 'aeiou']
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.string):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.string[index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
