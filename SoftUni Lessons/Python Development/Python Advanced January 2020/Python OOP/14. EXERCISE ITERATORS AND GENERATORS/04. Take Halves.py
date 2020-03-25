def solution():
    def integers():
        number = 1
        while True:
            yield number
            number += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        numbers = []
        for _ in range(n):
            numbers.append(next(seq))
        return numbers

    return take, halves, integers

