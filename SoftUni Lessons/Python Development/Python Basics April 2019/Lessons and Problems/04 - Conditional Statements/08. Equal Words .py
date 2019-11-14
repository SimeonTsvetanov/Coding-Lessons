"""
Conditional Statements - Lab
Проверка: https://judge.softuni.bg/Contests/Practice/Index/1012#0

08. Equal Words

Условие:
Да се напише програма, която чете две думи, въведени от потребителя, и проверява дали са еднакви.
Да не се прави разлика между главни и малки думи. Да се изведе "yes" или "no".
"""

word_1 = input()
word_2 = input()

if word_1.lower() == word_2.lower():
    print("yes")
else:
    print("no")
