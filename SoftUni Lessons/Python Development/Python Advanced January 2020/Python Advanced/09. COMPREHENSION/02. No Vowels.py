def no_vowels():
    print("".join([letter for letter in input() if letter not in ['a', 'o', 'u', 'e', 'i']]))


if __name__ == '__main__':
    no_vowels()
