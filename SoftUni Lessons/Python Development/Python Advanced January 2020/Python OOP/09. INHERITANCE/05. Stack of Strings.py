# There is a problem in this task, because the stack in other languages is printed in reverse.

"""
Create a class Stack which can store only strings and has the following functionality:
•	Private field: data: list
•	Public method: push(item)
•	Public method: pop()
•	Public method: peek()
•	Public method: is_empty(): returns boolean
"""


class Stack:
    def __init__(self):
        self.__data = []

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        result = self.__data.pop()
        return result

    def peek(self):
        return self.__data[-1]

    def is_empty(self):
        return self.__data == 0

