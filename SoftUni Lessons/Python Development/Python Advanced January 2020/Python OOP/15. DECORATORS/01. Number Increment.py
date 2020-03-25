def number_increment(numbers):
    def increase():
        for num in range(0, len(numbers)):
            numbers[num] += 1
        return numbers
    return increase()


print(number_increment([1, 2, 3]))  # Expected output: [2,3,4]
