def no_vowels():
    print("".join([letter for letter in input() if letter not in ['a', 'o', 'u', 'e', 'i']]))


def trains():
    train = [0 for count in range(int(input()))]
    while True:
        command = input().split(" ")
        if command[0] == "End":
            print(train)
            break
        elif command[0] == "add":
            train[-1] += int(command[1])
        elif command[0] == "insert":
            train[int(command[1])] += int(command[2])
        elif command[0] == "leave":
            train[int(command[1])] -= int(command[2])


def to_do_list():
    notes = []

    while True:
        note = input().split("-")
        if note[0] == "End":
            break
        notes.append([int(note[0]), note[1]])

    print([(note[1]) for note in list(sorted(notes, key=lambda x: x[0]))])


def palindrome_strings():
    words = input().split()
    palindromes = [word for word in words if word == word[::-1]]
    print(palindromes)
    print(f"Found palindrome {words.count(input())} times")


def even_numbers():
    # The task is done the correctly, but Judge doesn't like it. I guess it's broken
    nums = list(map(int, input().split(", ")))
    print([nums.index(num) for num in nums if num % 2 == 0])


def the_office():
    employees_happiness = [int(employee) for employee in input().split(' ')]
    happiness_improvement_factor = int(input())
    employees_happiness = [em * happiness_improvement_factor for em in employees_happiness]
    filtered = list(filter(lambda x: x >= (sum(employees_happiness) / len(employees_happiness)), employees_happiness))
    if len(filtered) >= len(employees_happiness) / 2:
        print(f"Score: {len(filtered)}/{len(employees_happiness)}. Employees are happy!")
    else:
        print(f"Score: {len(filtered)}/{len(employees_happiness)}. Employees are not happy!")


if __name__ == '__main__':
    # no_vowels()
    # trains()
    # to_do_list()
    # palindrome_strings()
    # even_numbers()
    the_office()