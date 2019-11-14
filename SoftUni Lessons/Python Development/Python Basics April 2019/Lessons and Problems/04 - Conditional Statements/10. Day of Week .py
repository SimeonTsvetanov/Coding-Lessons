"""
Conditional Statements - Lab
Проверка: https://judge.softuni.bg/Contests/Practice/Index/1012#0

10. Day of Week

Условие:
Напишете програма, която чете цяло число, въведено от потребителя, и отпечатва ден от седмицата (на английски език),
в граници [1...7] или отпечатва "Error" в случай, че въведеното число е невалидно.
Примерен вход и изход
Вход	Изход
1	Monday
2	Tuesday
3	Wednesday
4	Thursday
5	Friday
6	Saturday
7	Sunday
-1	Error
"""

day = int(input())

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Error")
