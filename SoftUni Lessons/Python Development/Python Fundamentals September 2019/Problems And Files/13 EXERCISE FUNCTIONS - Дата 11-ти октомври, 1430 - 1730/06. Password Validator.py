"""
Functions - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1728#5

SUPyF2 Functions-Exercise - 06. Password Validator

Problem:
Write a function that checks if a given password is valid. Password validations are:
•	The length should be 6 - 10 characters (inclusive)
•	It should consists only letters and digits
•	It should have at least 2 digits
If a password is valid print "Password is valid".
If it is NOT valid, for every unfulfilled rule print a message:
•	"Password must be between 6 and 10 characters"
•	"Password must consist only of letters and digits"
•	"Password must have at least 2 digits"

Examples:
Input:	        Output:

logIn	    Password must be between 6 and 10 characters
            Password must have at least 2 digits

MyPass123	Password is valid

Pa$s$s	    Password must consist only of letters and digits
            Password must have at least 2 digits
"""


def password_validator(password):
    valid_length = False
    only_letters_and_digits = False
    at_least_2_digits = False

    if 6 <= len(password) <= 10:
        valid_length = True
    else:
        print("Password must be between 6 and 10 characters")
    if password.isalnum():
        only_letters_and_digits = True
    else:
        print("Password must consist only of letters and digits")
    if len([digit for digit in password if digit.isdigit()]) >= 2:
        at_least_2_digits = True
    else:
        print("Password must have at least 2 digits")
    if valid_length and only_letters_and_digits and at_least_2_digits:
        print("Password is valid")


password_validator(input())

