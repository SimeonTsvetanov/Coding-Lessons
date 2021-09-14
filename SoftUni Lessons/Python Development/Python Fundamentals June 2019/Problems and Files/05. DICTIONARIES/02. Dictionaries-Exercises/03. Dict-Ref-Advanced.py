"""
Dictionaries - Exercises
Проверка: https://judge.softuni.bg/Contests/Practice/Index/1088#2

SUPyF Dictionaries Exercises - 03. Dict-Ref-Advanced

Problem:
Remember the Dict-Ref Problem from the previous exercise? Well this one is an Advanced Version.
You will begin receiving input lines containing information in one of the following formats:
- {key} -> {value 1, value 2, …, value n}
- {key} -> {otherKey}
The keys will always be strings, and the values will always be integers, separated by a comma and a space.
If you are given a key and values, you must store the values to the given key. If the key already exists,
you must add the given values to the old ones.
If you are given a key and another key, you must copy the values of the other key to the first one.
If the other key does not exist, this input line must be IGNORED.
When you receive the command “end”, you must stop reading input lines, and you must print all keys with their values,
in the following format:
- {key} === {value1, value2, value3. . .}

Examples:
    INPUT <<<
Isacc -> 5, 4, 3
Peter -> 6, 3, 3
Derek -> 2, 2, 2
end
    OUTPUT >>>
Isacc === 5, 4, 3
Peter === 6, 3, 3
Derek === 2, 2, 2

    INPUT <<<
Donald -> 2, 2, 2
Isacc -> 1
George -> John
John -> Isacc
end
    OUTPUT >>>
Donald === 2, 2, 2
Isacc === 1
John === 1
"""
di = {}

while True:
    input_line = input()
    if input_line == "end":
        break
    d = [item for item in input_line.split(" -> ")]
    if (not d[1].isalpha()) and (d[0] not in di):
        di[d[0]] = [int(item) for item in d[1].split(", ")]
    elif (not d[1].isalpha()) and (d[0] in di):
        values = [int(item) for item in d[1].split(", ")]
        di[d[0]] += [int(item) for item in d[1].split(", ")]
    elif d[1].isalpha() and (d[1] not in di):
        continue
    elif d[1].isalpha() and d[1] in di:
        di[d[0]] = [int(item) for item in di[d[1]]]

for k, v in di.items():
    print(f"{k} === ", end="")
    print(", ".join(str(o) for o in v))


def another_solution():
    dictionary = {}

    while True:
        command = input().split(" -> ")
        if command[0] == "end":
            break

        key = command[0]
        if command[1].isalpha():
            # Then its another Key
            other_key = command[1]
            if other_key in dictionary.keys():
                dictionary[key] = dictionary[other_key].copy()
        else:
            # Its a Values
            values = [int(value) for value in command[1].split(", ")]
            if key not in dictionary.keys():
                dictionary[key] = values
            else:
                dictionary[key].extend(values)

    for key, values in dictionary.items():
        print(f"{key} === {', '.join([str(value) for value in values])}")


# another_solution()
