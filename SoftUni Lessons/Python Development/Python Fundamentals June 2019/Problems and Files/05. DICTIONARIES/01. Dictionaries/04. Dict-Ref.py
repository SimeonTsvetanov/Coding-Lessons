"""
Dictionaries and Functional Programming
Проверка: https://judge.softuni.bg/Contests/Practice/Index/945#3

SUPyF Dictionaries - 04. Dict-Ref

Problem:
You have been tasked to create a referenced dictionary, or in other words a dictionary,
 which knows how to reference itself.
You will be given several input lines, in one of the following formats:
- {name} = {value}
- {name} = {secondName}
The names will always be strings, and the values will always be integers.
In case you are given a name and a value, you must store the given name and its value. If the name already EXISTS,
 you must CHANGE its value with the given one.
In case you are given a name and a second name, you must store the given name with the same value as the value
 of the second name. If the given second name DOES NOT exist, you must IGNORE that input.
When you receive the command “end”, you must print all entries with their value, by order of input, in the following
format:
{entry} === {value}

Examples:
    ----------------------------------
Input:                  Output:
Cash = 500              Cash === 200
Johny = 5               Johny === 5
Cash = 200              Johnny === 200
Johnny = 200            Car === 150
Car = 150               Plane === 2000000
Plane = 2000000
end
    ----------------------------------
  Input:                  Output:
Entry1 = 10000            Entry1 === 10000
Entry2 = 12345            Entry2 === 10101
Entry3 = 10101            Entry3 === 10000
Entry4 = Entry1           Entry4 === 10000
Entry2 = Entry3
Entry3 = Entry4
end
    ----------------------------------
"""
# There are 2 Different approaches for the problem that I've used. :)
"""
input_line = input()

dictionary = {}

while not input_line == "end":
    data = [item for item in input_line.split(" = ")]

    if data[1].isdigit():
        dictionary[data[0]] = int(data[1])
    else:
        if data[1] in dictionary:
            dictionary[data[0]] = int(dictionary.get(data[1]))

    input_line = input()

for key in dictionary:
    print("{0} === {1}".format(key, dictionary[key]))
"""

dict_ref = {}
while True:
    command = input()
    if command == "end":
        break
    list_command = [item for item in command.split(" = ")]
    word_command = list_command[1]
    if list_command[1] in dict_ref.keys():
        if list_command[0] in dict_ref.keys() and list_command[1] not in dict_ref.keys():
            continue
        else:
            dict_ref[list_command[0]] = dict_ref[list_command[1]]
    elif list_command[0] not in dict_ref.keys() and list_command[1] not in dict_ref.keys() and \
            not 48 <= ord(word_command[0]) <= 57:
        continue
    elif list_command[0] in dict_ref and list_command[1] not in dict_ref and \
            48 <= ord(word_command[0]) <= 57:
        dict_ref[list_command[0]] = list_command[1]
    elif list_command[0] not in dict_ref.keys() and list_command[1] not in dict_ref.keys() \
            and 48 <= ord(word_command[0]) <= 57:
        dict_ref[list_command[0]] = list_command[1]
    else:
        continue

for key, value in dict_ref.items():
    print(f"{key} === {int(value)}")


