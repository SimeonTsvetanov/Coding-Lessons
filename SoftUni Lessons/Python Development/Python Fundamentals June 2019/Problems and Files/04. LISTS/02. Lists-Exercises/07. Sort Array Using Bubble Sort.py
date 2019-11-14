"""
Lists
Check your answer: https://judge.softuni.bg/Contests/Practice/Index/426#3

04.	Sort Array Using Bubble Sort

Problem:
Read a list of integers on the first line of the console. After that, sort the list, using the Bubble Sort algorithm.
Examples
Input	            Output
5 3 4 1 2	        1 2 3 4 5
11 872 673 1 2	    1 2 11 673 872
11 52 43 12 1 6	    1 6 11 12 43 52
"""


def short_bubble_sort(a_list):
    exchanges = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
        pass_num = pass_num - 1


nums = [int(item) for item in input().split(" ")]
short_bubble_sort(nums)

for num in nums:
    print(num, end=" ")

