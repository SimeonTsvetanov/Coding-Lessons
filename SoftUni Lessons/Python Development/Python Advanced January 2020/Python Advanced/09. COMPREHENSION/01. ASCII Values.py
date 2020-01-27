def read_input():
    words = input().split(", ")
    return words


def ascii_values(words_list):
    """
    This solution will return a dictionary with:
    key - the element it self,
    value - it's ASCII values.
    """
    ascii_values_dict = {word: ord(word) for word in words_list}
    print(ascii_values_dict)


def occurrences(words_list):
    """
    This solution will create a dictionary with:
    key - the element it self,
    Value - times it occurs in the list.
    """
    occurrences_dict = {word: words_list.count(word) for word in words_list}
    print(occurrences_dict)


def solve():
    ascii_values(read_input())
    occurrences(read_input())


if __name__ == '__main__':
    solve()
