"""
Lists Basics - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1724#1

SUPyF2 Lists Basics Lab - 02. Strange Zoo

Problem:
You are at the zoo and the meerkats look strange. You will receive 3 strings: (tail, body, head).
You have to re-arrange the elements in a list, so that the animal looks normal again: (head, body, tail)

Example:
Input:
my tail
my body seems on place
my head is on the wrong end!
Output:
['my head is on the wrong end!','my body seems on place','my tail']

Input:
tail
body
head
Output:
['head', 'body', 'tail']
"""
tail = input()
body = input()
head = input()
my_list = [head, body, tail]
print(my_list)
