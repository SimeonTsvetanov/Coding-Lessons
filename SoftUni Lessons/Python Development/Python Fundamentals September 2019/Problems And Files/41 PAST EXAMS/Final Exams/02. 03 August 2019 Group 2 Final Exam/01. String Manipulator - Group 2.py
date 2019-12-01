"""
Programming Fundamentals Final Exam - 03 August 2019 Group 2
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1749#0
Name: String Manipulator - Group 2
"""


string = input()


def change(char: str, replacement: str):
    global string
    string = string.replace(char, replacement)
    print(string)


def includes(string_to_include: str):
    if string_to_include in string:
        print("True")
    else:
        print("False")


def end(end_string):
    if string.endswith(end_string):
        print("True")
    else:
        print("False")


def uppercase():
    global string
    string = string.upper()
    print(string)


def find_index(char):
    print(string.index(char))


def cut(start_index: int, length: int):
    global string
    end_index = start_index + length
    string = string[start_index:end_index]
    print(string)


def run():
    while True:
        command = input().split()
        if command[0] == "Done":
            break

        elif command[0] == "Change":
            change(char=command[1], replacement=command[2])

        elif command[0] == "Includes":
            includes(string_to_include=command[1])

        elif command[0] == "End":
            end(end_string=command[1])

        elif command[0] == "Uppercase":
            uppercase()

        elif command[0] == "FindIndex":
            find_index(char=command[1])

        elif command[0] == "Cut":
            cut(start_index=int(command[1]), length=int(command[2]))


if __name__ == '__main__':
    run()
