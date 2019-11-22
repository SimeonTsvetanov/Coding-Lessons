"""
Regular Expressions - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1742#3

SUPyF2 RegEx-Lab - 04. Match Numbers

Problem:
Write a program, which finds all integer and floating-point numbers in a string.
Compose the Regular Expression
A number has the following characteristics:
•	Has either whitespace before it or the start of the string (match either ^ or what's called a positive lookbehind).
The entire syntax for the beginning of your RegEx might look something like "(^|(?<=\s))".
•	The number might or might not be negative, so it might have a hyphen on its left side ("-").
•	Consists of one or more digits.
•	Might or might not have digits after the decimal point
•	The decimal part (if it exists) consists of a period (".") and one or more digits after it. Use a capturing group.
•	Has either whitespace before it or the end of the string (match either $ or what's called a positive lookahead).
        The syntax for the end of the RegEx might look something like "($|(?=\s))".
Let's see how we would translate the above rules into a regular expression:
•	First off, we need to establish what needs to exist before our number. We can't use \b here, since it includes "-",
    which we need to match negative numbers.
Instead, we'll use a positive lookbehind, which matches if there's something immediately behind it.
    We'll match if we're either at the start of the string (^), or if there's any whitespace behind the string:
--- (^\?<=\s)
•	Next, we'll check whether there's a hyphen, signifying a negative number:
--- (^|(?<=\s))-?
Since having a negative sign isn't required, we'll use the "?" quantifier, which means "between 0 and 1 times".
•	After that, we'll match any integers – naturally, consisting one or more digits:
--- (^|(?<=\s))-?\d+
•	Next, we'll match the decimal part of the number, which might or might not exist
    (note: we need to escape the period character, as it's used for something else in RegEx):
--- (^|(?<=\s))-?\d+(V\d+)?
•	Finally, we're going to use the same logic for the end of our string as the start –
    we're going to match only if the number has either a whitespace or the end of the string ("$"):
--- (^|(?<=\s))-?\d+(V\d+)?($|(?=\s))

Examples:
    Input:
    1 -1 1s 123 s-s -123 _55_ _f 123.456 -123.456 s-1.1 s2 -1- zs-2 s-3.5
    Output:
    1 -1 123 -123 123.456 -123.456
"""
import re

text = input()

# We can break the groups into parts to make it easier:
prefix_pattern = r"(^|(?<=\s))"
number_pattern = r"(?P<number>-?\d+([.]\d+)?)"
suffix_pattern = r"($|(?=\s))"
pattern = prefix_pattern + number_pattern + suffix_pattern

# Or just use it as a whole:
# pattern = r"(^|(?<=\s))(?P<number>-?\d+([.]\d+)?)($|(?=\s))"

matches = re.finditer(pattern, text)
numbers = [match.group("number") for match in matches]

print(" ".join(numbers))
