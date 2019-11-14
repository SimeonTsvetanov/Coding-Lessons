"""
Dictionaries - Exercises
Проверка: https://judge.softuni.bg/Contests/Practice/Index/1088#0

SUPyF Dictionaries Exercises - 01. Key-Key Value-Value

Problem:
Write a program, which searches for a key and value inside of several key-value pairs.
Input
- On the first line, you will receive a key.
- On the second line, you will receive a value.
- On the third line, you will receive N.
- On the next N lines, you will receive strings in the following format:
“key => {value 1};{value 2};…{value X}”
After you receive N key -> values pairs, your task is to go through them and print only the keys,
which contain the key and the values, which contain the value. Print them in the following format:
{key}:
-{value1}
-{value2}
…
-{valueN}

Examples:

INPUT:                              OUTPUT:
bug                                 debug:
X                                   -XUL
3                                   -XC
invalidkey => testval;x;y           buggy:
debug => XUL;ccx;XC                 -testX
buggy => testX;testY;XtestZ         -XtestZ

INPUT:
key
valu
2
xkeyc => value;value;valio
keyhole => valuable;x;values

INPUT:                              OUTPUT:
key                                 xkeyc:
valu                                -value
2                                   -value
xkeyc => value;value;valio          keyhole:
keyhole => valuable;x;values        -valuable
                                    -values
"""

key = input()
value = input()
n = int(input())

dictionary = {}

for i in range(n):
    a = [item for item in input().split(" => ")]
    key_check = a[0]
    value_check = [item for item in a[1].split(";")]

    if key in key_check:
        dictionary[key_check] = []
        for item in value_check:
            if value in item:
                if len(dictionary[key_check]) == 0:
                    dictionary[key_check] = [item]
                elif len(dictionary[key_check]) != 0:
                    dictionary[key_check] += [item]

for key, value in dictionary.items():
    print(f"{key}:")
    for item in value:
        print(f"-{item}")
