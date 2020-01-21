def solve_with_set():  # Solution with SET:
    letters_set = set()
    text = input()

    for letter in text:
        letters_set.add(letter)

    for letter in sorted(letters_set):
        print(f"{letter}: {text.count(letter)} time/s")


def solve_with_dictionary():  # Solution with Dictionary:
    dict_letters = {}
    text = input()
    for letter in text:
        if letter not in dict_letters:
            dict_letters[letter] = 1
        else:
            dict_letters[letter] += 1
    for letter, count in sorted(dict_letters.items()):
        print(f"{letter}: {count} time/s")


if __name__ == '__main__':
    solve_with_set()
    # solve_with_dictionary()
