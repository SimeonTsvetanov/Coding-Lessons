"""
Functions and Debugging
Проверка: https://judge.softuni.bg/Contests/Compete/Index/922#2

03. Printing Triangle

Условие:
03. Printing Triangle
Create a function for printing triangles as shown below:
Examples
Input:
3
Output:
1
1 2
1 2 3
1 2
1

Input:
4
Output:
1
1 2
1 2 3
1 2 3 4
1 2 3
1 2
1
"""

num = int(input())


def triangle():
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(f"{j}", end=" ")
        print()
    for i in range(num - 1, 0, -1):
        for j in range(1, i + 1):
            print(f"{j}", end=" ")
        print()


triangle()

# def triangle(number):
#     for i in range(1, number + 1):
#         for j in range(1, i + 1):
#             print(f"{j}", end=" ")
#         print()
#     for i in range(number - 1, 0, -1):
#         for j in range(1, i + 1):
#             print(f"{j}", end=" ")
#         print()
# 
# 
# triangle(number=int(input()))


