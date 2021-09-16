def which_are_in():
    words_to_look_for = input().split(", ")
    words_to_look_in = input().split(", ")

    found = []
    for word_to_find in words_to_look_for:
        for word_to_check in words_to_look_in:
            if word_to_find in word_to_check and word_to_find not in found:
                found.append(word_to_find)

    print(found)


def next_version():
    # The basic version:
    """
    n1, n2, n3 = list(map(int, input().split(".")))
    n3 += 1
    if n3 == 10:
        n3 = 0
        n2 += 1
        if n2 == 10:
            n2 = 0
            n1 += 1

    print(f"{n1}.{n2}.{n3}")
    """

    # And the advanced version:
    print('.'.join(str(num) for num in str((int(''.join([str(elem) for elem in input().split(".")])) + 1))))


def word_filter():
    print("\n".join([word for word in input().split() if len(word) % 2 == 0]))


def number_classification():
    numbers = list(map(int, input().split(", ")))
    print(f"Positive: {', '.join([str(num) for num in numbers if num >= 0])}")
    print(f"Negative: {', '.join([str(num) for num in numbers if num < 0])}")
    print(f"Even: {', '.join([str(num) for num in numbers if num % 2 == 0])}")
    print(f"Odd: {', '.join([str(num) for num in numbers if num % 2 != 0])}")


def office_chairs():
    game_on = True
    chairs_left = 0

    for room in range(1, int(input()) + 1):
        command = input().split(" ")
        chairs = len(command[0])
        visitors = int(command[1])

        if chairs >= visitors:
            chairs_left += chairs - visitors
        else:
            game_on = False
            print(f"{visitors - chairs} more chairs needed in room {room}")

    if game_on:
        print(f"Game On, {chairs_left} free chairs left")


def electron_distribution():
    total = int(input())

    array = []
    n = 1

    while total > 0:
        el = 2 * (n ** 2)
        if el <= total:
            array.append(el)
            total -= el
        else:
            array.append(total)
            total -= el
        n += 1

    print(array)


def group_of_10s():
    nums = [int(num) for num in input().split(", ")]
    boundary = 10
    group = []

    while True:
        if len(nums) == 0:
            break
        for num in nums:
            if (boundary - 10) < num <= boundary:
                group.append(num)
        print(f"Group of {boundary}'s: {group}")
        boundary += 10
        [nums.remove(num) for num in group]
        group = []


def decipher_this():
    # create a list for the deciphered words
    # loop all the words from the input
    # for each word loop the letters
    # make a list from numbers from the loop and change it to the letter it represents
    # make a list from letters from the loop and change the first with the last
    # join the first to the second list and then add them and at the list with deciphered words
    # print them

    deciphered_words = []
    for coded_word in input().split(" "):
        first_letter = chr(int("".join([symbol for symbol in coded_word if symbol.isdigit()])))
        rest = [symbol for symbol in coded_word if symbol.isalpha()]
        rest[0], rest[-1] = rest[-1], rest[0]
        deciphered_words.append(first_letter + ''.join(rest))
    print(' '.join(deciphered_words))


if __name__ == '__main__':
    # which_are_in()
    # next_version()
    # word_filter()
    # number_classification()
    # office_chairs()
    # electron_distribution()
    # group_of_10s()
    # decipher_this()
    # The rest of the tasks are to long to solve again. 