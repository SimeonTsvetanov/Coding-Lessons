"""
Functions - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1728#6

SUPyF2 Functions-Exercise - 07. Perfetct Number

Problem:
Write a function that receives an integer number and returns if this number is perfect or NOT.
A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
That is the sum of its positive divisors excluding the number itself (also known as its aliquot sum).

Examples:
Input:	    Output: 	                 Comments:
6	        We have a perfect number!	 1 + 2 + 3
28	        We have a perfect number!	 1 + 2 + 4 + 7 + 14
1236498	    It's not so perfect.
Hint
Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself) => 6 is a perfect number, because it is the sum of 1 + 2 + 3 (all of which are divided without residue).
•	Read about the Perfect number here: https://en.wikipedia.org/wiki/Perfect_number

"""


def perfect_number(number):
    result = 0
    for i in range(1, number):
        if number % i == 0:
            result = result + i
    if result == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


perfect_number(int(input()))
