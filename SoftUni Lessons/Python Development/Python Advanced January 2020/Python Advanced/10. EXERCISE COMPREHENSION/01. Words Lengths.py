def solve_words_length():
    strings_dict = {word: len(word) for word in input().split(", ")}
    print(', '.join([f"{word} -> {length}" for word, length in strings_dict.items()]))


if __name__ == '__main__':
    solve_words_length()

