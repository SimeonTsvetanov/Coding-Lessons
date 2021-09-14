"""
Functions and Debugging
Проверка: https://judge.softuni.bg/Contests/Compete/Index/922#6

07. Greater of Two Values

Условие:
You are given two values of the same type as input. The values can be of type int, char of string.
Create a function that returns the greater of the two values:

Examples
Input:
int
2
16
Output:
16

Input:
char
a
z
Output:
Z

Input:
string
Ivan
Todor
Output:
Todor

Hints
1.	For this function you need to create three functions with the same name and different signatures
2.	Create a function which will compare integers.
3.	Lastly you need to create a function to compare the other types.
4.	The last step is to read the input, use appropriate variables and call the function you’ve just written.
"""


def compare(type_value = input(), value_1 = input(), value_2 = input()):
    if type_value == "int":
        if int(value_1) > int(value_2):
            return print(value_1)
        return print(value_2)
    elif type_value == "char":
        if ord(value_1) > ord(value_2):
            return print(value_1)
        return print(value_2)
    elif type_value == "string":
        if value_1 > value_2:
            return print(value_1)
        return print(value_2)


    # """
# You are given two values of the same type as input. The values can be of type int, char of string.
# Create a function that returns the greater of the two values:
# """
# 
# 
# def compare_int(first, second):
#     print(first) if int(first) > int(second) else print(second)
# 
# 
# def compare_char(first, second):
#     print(first) if first > second else print(second)
# 
# 
# def compare_string(first, second):
#     print(first) if first > second else print(second)
# 
# 
# def run():
#     type_to_compare = input()
#     first = input()
#     second = input()
# 
#     if type_to_compare == "int":
#         compare_int(first, second)
#     elif type_to_compare == "char":
#         compare_char(first, second)
#     elif type_to_compare == "string":
#         compare_string(first, second)
# 
# 
# if __name__ == '__main__':
#     run()
