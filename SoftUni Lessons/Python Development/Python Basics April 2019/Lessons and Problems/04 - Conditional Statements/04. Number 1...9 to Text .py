"""
Conditional Statements - Lab
Проверка: https://judge.softuni.bg/Contests/Practice/Index/1012#0

04. Number 1...9 to Text

Условие:
Да се напише програма, която чете цяло число в диапазона [1…9],
въведено от потребителя и го изписва с думи на английски език.
Ако числото е извън диапазона, програмата изписва "number too big".
Примерен вход и изход
5	five		1	one		9	nine		10	number too big
"""

num = int(input())

if num == 1:
    print("one")
elif num == 2:
    print("two")
elif num == 3:
    print("three")
elif num == 4:
    print("four")
elif num == 5:
    print("five")
elif num == 6:
    print("six")
elif num == 7:
    print("seven")
elif num == 8:
    print("eight")
elif num == 9:
    print("nine")
else:
    print("number too big")
