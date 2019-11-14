"""
Lists
Check your answer: https://judge.softuni.bg/Contests/Practice/Index/425#3

04. Ununion Lists

Problem:
You will be given a sequence of integers, separated by a space. This is the primal list.
Then you will receive an integer N. On the next N lines, you will receive sequences of integers.
Your task is to add all elements that the primal list does not contain from the current sequence to the primal list
and then remove from the primal list, all elements which are contained in the current sequence of integers.
If there are several occurrences, remove all occurrences you find.
After you are done receiving lists and manipulating the primal list, sort the primal list and print it.

"""

nums = [int(item) for item in input().split(" ")]
count_times = int(input())

while True:
    if count_times == 0:
        break
    current_sequence = [int(item) for item in input().split(" ")]
    for current_num in current_sequence:
        if current_num not in nums:
            nums += [current_num]
        elif current_num in nums:
            while current_num in nums:
                nums.remove(current_num)
    count_times -= 1

nums.sort()
for num in nums:
    print(num, end=" ")
