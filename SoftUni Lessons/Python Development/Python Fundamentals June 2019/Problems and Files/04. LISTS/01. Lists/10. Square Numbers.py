"""
Lists
Check your answer: https://judge.softuni.bg/Contests/Practice/Index/924#9

10. Square Numbers

Problem:
Read a list of integers and extract all square numbers from it and print them in descending order.
A square number is an integer which is the square of any integer. For example, 1, 4, 9, 16 are square numbers.
Examples
Input	                    Output
3 16 4 5 6 8 9 	            16 9 4
12 1 9 4 16 8 25 49 16	    49 25 16 16 9 4 1
"""

"""
How I solved it:

First we will take all the added integers on one line divided by space and it will add them in a new list one by one:
Then we need to create a second list which will contain all the numbers we want.
Then using a For Loop we will check for each number in the first list if the number 
is bigger than 0(<0 can't be a perfect square (and it will crash :()) AND one wicked formula to check if the number
is a square number. And then if both are True to add them in the new List.
Then we need to organise the list in descending order using (.sort(reverse=True)).
And Finally to print it, we will use a for loop. So they can be printed on one line with blank space in between. 
"""
nums = [int(item) for item in input().split(" ")]
square_numbers = []

for num in nums:
    if num > 0 and int(num**0.5)**2 == int(num):
        square_numbers += [num]

square_numbers.sort(reverse=True)

for square_number in square_numbers:
    print(square_number, end=" ")


# nums = [int(num) for num in input().split(" ") if int(num) > 0]
# squares = [num for num in nums if (num**0.5) % 1 == 0]
# print(*sorted(squares, reverse=True))
