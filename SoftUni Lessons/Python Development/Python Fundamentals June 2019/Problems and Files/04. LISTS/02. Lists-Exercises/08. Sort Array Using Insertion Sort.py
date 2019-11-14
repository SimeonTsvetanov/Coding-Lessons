"""
Lists
Check your answer: https://judge.softuni.bg/Contests/Practice/Index/426#4

05. Sort Array Using Insertion Sort

Problem:
Read a list of integers on the first line of the console. After that, sort the list, using the Insertion Sort algorithm.
Examples
Input	            Output
5 3 4 1 2	        1 2 3 4 5
11 872 673 1 2	    1 2 11 673 872
11 52 43 12 1 6	    1 6 11 12 43 52
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


nums = [int(item) for item in input().split(" ")]
insertion_sort(nums)

for num in nums:
    print(num, end=" ")
