"""
Functions and Debugging
Проверка: https://judge.softuni.bg/Contests/Compete/Index/922#5

06. Math Power

Условие:
Create a function that calculates and returns the value of a number raised to a given power:

Examples
Input:
2
8
Output:
256.0
Input:
1.5
3
Output:
3.375

Hints
1.	As usual, read the input
2.	Create a function which will have two parameters - the number and the power, and will return a result
3.	Print the result with no specific formatting.
"""

# Това е по - чистият вариянт :):
# В тази опция само ако се извика функцията, както по- долу: math_power(). Тогава ще се търси инпут, ще смята и ще
# върне резултата.

# def math_power(num=(int(input())), power=int(input())):
#    total = num ** power
#    print(f"{total}")


# math_power()


def math_power(num, on_power):
    result = num ** on_power
    return result


numbers_to_turn = math_power(float(input()), int(input()))

print(numbers_to_turn)

