"""
Lists Advanced - More Exercises
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1732#1

SUPyF2 Lists Advanced-More-Ex. - 02. Car Race

Problem:
You will be given a list of numbers and a string.
For each element of the list you have to calculate the sum of its digits and take the element,
corresponding to that index from the text. If the index is greater than the length of the text,
start counting from the beginning (so that you always have a valid index). Then you get that element from the text,
you must remove the character you have taken from it (so for the next index, the text will be with one character less).
Example:
Input:	                           Output:
9992 562 8933                      hey
This is some message for you
"""
digits = input().split()
text = [letter for letter in input()]
message = ""
for digit in digits:
    number = sum([int(num) for num in digit])
    condition = False
    while True:
        if condition:
            break
        if number <= len(text):
            message += text[number]
            text.pop(number)
            condition = True
        else:
            number -= len(text)

print(message)
