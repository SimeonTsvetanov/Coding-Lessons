"""
Lists Advanced - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1731#2

SUPyF2 Lists-Advanced-Exercise - 03. Next Version

Problem:
You're fed up about changing the version of your software manually.
Instead, you will create a little script that will make it for you.
You will be given a version as in this example: "1.3.4".
You have to find the next version and print it ("1.3.5" from the example).
The only rule is that the numbers cannot be greater than 9.
If that happens, set the current number to 0 and increase the number before it.
For more clarification, see the examples. Note: there will be no case where the first number will get greater than 9

Example
Input	Output
1.2.3	1.2.4
1.3.9	1.4.0
3.9.9	4.0.0
"""
nums_list = [digit for digit in input().split(".")]
number = ""
for num in nums_list:
    number += num
print(".".join([digit for digit in str(int(number) + 1)]))




