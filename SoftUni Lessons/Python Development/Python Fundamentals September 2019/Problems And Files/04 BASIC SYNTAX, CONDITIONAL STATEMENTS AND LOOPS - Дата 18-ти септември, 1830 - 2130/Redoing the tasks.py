def largest_of_three_numbers():
    print(max(int(input()), int(input()), int(input())))


def number_definer():
    num = float(input())

    if num == 0:
        print("zero")
    elif num > 0:
        if num < 1:
            print("small positive")
        elif num > 1000000:
            print("large positive")
        else:
            print("positive")
    elif num < 0:
        if abs(num) < 1:
            print("small negative")
        elif abs(num) > 1000000:
            print("large negative")
        else:
            print("negative")


def word_reverse():
    print("".join(reversed([letter for letter in input()])))


def number_between_1_and_100():
    while True:
        num = float(input())
        if 1 <= num <= 100:
            print(f"The number {num} is between 1 and 100")
            break


def patterns():
    num = int(input())
    for row in range(1, num + 1):
        print(row * "*")
    for row in range(num - 1, 0, -1):
        print(row * "*")


# largest_of_three_numbers()
# number_definer()
# word_reverse()
# number_between_1_and_100()
# patterns()
