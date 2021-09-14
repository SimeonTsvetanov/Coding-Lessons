"""
Lists
Проверка: https://judge.softuni.bg/Contests/Practice/Index/924#6

07. Remove Negatives and Reverse

Условие:
Read a list of integers, remove all negative numbers from it and print the remaining items in reversed order.
In case of no items left in the list, print “empty”.
Examples
Input	            Output
10 -5 7 9 -33 50	50 9 7 10
7 -2 -10 1	        1 7
-1 -2 -3	        empty
Hints
-Read the list
-Create a new empty list for the results.
-Scan the input list from the end to the beginning. Check each item and append all non-negative items to the result list.
-Finally, print the results list (at a single line holding space-separated numbers).
"""

"""
How I solved it:

First we will take all the added integers on one line divided by space and it will add them in a new list one by one:
We will create a if_empty variable to check if the list is empty later.
Then using a  reversed() For Loop, we will make a if, else construction where if will check for negative numbers
and if there are some. It will remove them. Else it will print as they are positive and it will set the if empty
checker to False (since the List will still have numbers). And finally We will check if_empty is True and if so 
it will print "empty"  
"""

nums = [int(item) for item in input().split(" ") if int(item) > 0]
if nums:
    print(*reversed(nums))
else:
    print("empty")

# nums = [int(num) for num in input().split(" ") if int(num) >= 0][::-1]
# print(*nums) if nums else print("empty")




