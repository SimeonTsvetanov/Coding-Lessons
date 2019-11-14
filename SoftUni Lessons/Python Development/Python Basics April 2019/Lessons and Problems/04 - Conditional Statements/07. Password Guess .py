"""
Conditional Statements - Lab
Проверка: https://judge.softuni.bg/Contests/Practice/Index/1012#0

07. Password Guess

Условие:
Да се напише програма, която чете парола (един ред с произволен текст), въведена от потребителя и проверява дали
въведеното съвпада с фразата "s3cr3t!P@ssw0rd". При съвпадение да се изведе "Welcome".
При несъвпадение да се изведе "Wrong password!".
Примерен вход и изход
вход	изход		        вход	        изход		вход	    изход
qwerty	Wrong password!		s3cr3t!P@ssw0rd	Welcome		s3cr3t!p@ss	Wrong password!
"""

password_input = input()
PASSWORD = "s3cr3t!P@ssw0rd"

if PASSWORD == password_input:
    print("Welcome")
else:
    print("Wrong password!")
