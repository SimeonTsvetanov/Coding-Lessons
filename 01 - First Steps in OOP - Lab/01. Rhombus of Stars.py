class RhombusOfStars:
    def __init__(self, rows: int, value="*"):
        self.rows = rows
        self.value = value

    def __repr__(self):
        size = self.rows
        val = self.value
        result = ''
        for i in range(1, size):
            result += f"{' ' * (size - i)}{f'{val} ' * (size - (size - i))}\n"
        for i in range(size - 1, -1, -1):
            result += f"{' ' * (size - i - 1)}{f'{val} ' * (size - (size - i - 1))}\n"
        return result[:-1]


s = int(input())
rhomb = RhombusOfStars(rows=s)
print(rhomb)

