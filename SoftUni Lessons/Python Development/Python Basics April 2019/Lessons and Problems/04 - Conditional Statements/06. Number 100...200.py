"""
Conditional Statements - Lab
Проверка: https://judge.softuni.bg/Contests/Practice/Index/1012#0

06. Number 100...200

Условие:
Да се напише програма, която чете цяло число, въведено от потребителя, и проверява, дали е под 100,
между 100 и 200 или над 200. Да се отпечатат съответно съобщения, като в примерите по-долу:
Примерен вход и изход
вход	изход		    вход	изход		            вход	изход
95	    Less than 100	120	    Between 100 and 200		210	    Greater than 200
"""

num = int(input())

if num < 100:
    print("Less than 100")
elif 100 <= num <= 200:
    print("Between 100 and 200")
else:
    print("Greater than 200")


