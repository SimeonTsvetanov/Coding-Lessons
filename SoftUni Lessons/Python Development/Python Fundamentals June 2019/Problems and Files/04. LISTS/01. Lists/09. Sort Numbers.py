"""
Lists
Check your answer: https://judge.softuni.bg/Contests/Practice/Index/924#8

09. Sort Numbers

Problem:
Read a list of decimal numbers and sort them in increasing order. Print the output as shown in the examples below.
Examples
Input	    Output
8 2 7 3	    2 <= 3 <= 7 <= 8
2 4 -9	    -9 <= 2 <= 4
Hints
- Use the built-in method list.sort().
"""

"""
How I solved it:

First we will take all the added floats on one line divided by space and it will add them in a new list one by one:
then we need to use .sort() function to sort the items by which is bigger. 
Then we will create a checker that will be as big as the items count.
and Finally we will create a For cycle for each number in nums to be printed and after it it will print one blank 
space.
After that it will remove 1 from the checker and then it will check if the checker is equal to 0 and if not it will 
print the less Than or equal sign. (This is so that it wont print one extra <= after the last item in the list.)  
"""
nums = [float(item) for item in input().split(" ")]
nums.sort()
checker = len(nums)
for num in nums:
    print(int(num), end=" ")
    checker -= 1
    if checker == 0:
        break
    print(end="<= ")

# nums = sorted([int(num) for num in input().split(" ")])
# print(" <= ".join([str(num) for num in nums]))
