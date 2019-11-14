"""
Functions - More Exercises
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1729#3

SUPyF2 Functions-More-Exercises - 04. Tribonacci Sequence

Problem:
In the "Tribonacci" sequence, every number is formed by the sum of the previous 3.
You are given a number num. Write a program that prints num numbers from the Tribonacci sequence, each on a new line,
starting from 1. The input comes as a parameter named num. The value num will always be positive integer.
Examples
Input	Output		Input	Output
4	    1 1 2 4     8       1 1 2 4 7 13 24 44
"""


def tribonacci():
    num = int(input())
    tribonacci_list = []
    for i in range(num):
        if i == 0 or i == 1:
            tribonacci_list.append(1)
        elif i == 2:
            tribonacci_list.append(2)
        else:
            tribonacci_list.append(sum(tribonacci_list[-3:]))
    print(*tribonacci_list)


if __name__ == '__main__':
    tribonacci()

