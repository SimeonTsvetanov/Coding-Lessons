"""
Functions and Debugging
Проверка: https://judge.softuni.bg/Contests/Compete/Index/922#7

08. Multiply Evens by Odds

Условие:
Create a program that reads an integer number and multiplies the sum of all its even digits
by the sum of all its odd digits:

Examples
Input:
12345
Output:
54
Comments:
12345 has 2 even digits - 2 and 4. Even digits has sum of 6.
Also it has 3 odd digits - 1, 3 and 5. Odd digits has sum of 9.
Multiply 6 by 9 and you get 54.

Input:
-12345
Output:
54

Hints
1.	Create a function with a name describing its purpose. The function should have a single parameter and will
return value. Also the function will call two other functions.
2.	Create two other functions each of which will sum either even or odd digits.
3.	Implement the logic for summing odd digits.
4.	Do the same for the function that will sum even digits.
5.	As you test your solution you may notice that it doesn't work for negative numbers. Following the program execution
line by line, find and fix the bug.
"""

num = int(input())


def numbers():
    even_sum = 0
    odd_sum = 0
    for i in str(abs(num)):
        if int(i) % 2 == 0:
            even_sum += int(i)
        elif int(i) % 2 != 0:
            odd_sum += int(i)
    total_sum = even_sum * odd_sum
    return total_sum


print(numbers())

# """
# Create a program that reads an integer number and
# multiplies the sum of all its even digits by the sum of all its odd digits:
# """
# 
# 
# def multiply_even_by_odd():
#     number = abs(int(input()))
# 
#     even_sum = sum([int(num) for num in str(number) if int(num) % 2 == 0])
#     odd_sum = sum([int(num) for num in str(number) if int(num) % 2 != 0])
# 
#     print(even_sum * odd_sum)
# 
# 
# multiply_even_by_odd()

