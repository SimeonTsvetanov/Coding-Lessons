"""
Conditional Statements - Lab
Проверка: https://judge.softuni.bg/Contests/Practice/Index/1012#0

11. Animal Type

Условие:
Напишете програма, която отпечатва класа на животното според неговото име, въведено от потребителя.
-dog -> mammal
-crocodile, tortoise, snake -> reptile
-others -> unknown
Примерен вход и изход
Вход	Изход
dog	    mammal
snake	reptile
cat	    unknown
"""

animal = input()

if animal == "dog":
    print("mammal")
elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
    print("reptile")
else:
    print("unknown")
