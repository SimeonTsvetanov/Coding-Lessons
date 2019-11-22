"""
Regular Expressions - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1742#2

SUPyF2 RegEx-Lab - 03. Match Dates

Problem:
Write a program, which matches a date in the format "dd{separator}MMM{separator}yyyy".
Use capturing groups in your regular expression.
Compose the Regular Expression
Every valid date has the following characteristics:
•	Always starts with two digits, followed by a separator
•	After that, it has one uppercase and two lowercase letters (e.g. Jan, Mar).
•	After that, it has a separator and exactly 4 digits (for the year).
•	The separator could be either of three things: a period ("."), a hyphen ("-") or a forward slash ("/")
•	The separator needs to be the same for the whole date (e.g. 13.03.2016 is valid, 13.03/2016 is NOT).
        Use a group backreference to check for this.
You can follow the table below to help with composing your RegEx:

Match ALL of these:
13/Jul/1928, 10-Nov-1934, 25.Dec.1937
Match NONE of these:
01/Jan-1951, 23/sept/1973, 1/Feb/2016

Use capturing groups for the day, month and year.
Since this problem requires more complex RegEx, which includes named capturing groups,
we'll take a look at how to construct it:
•	First off, we don't want anything at the start of our date, so we're going to use a word boundary "\b":
--- \b
•	Next, we're going to match the day, by telling our RegEx to match exactly two digits,
and since we want to extract the day from the match later, we're going to put it in a capturing group:
--- \b(\d{2})
•	Next comes the separator – either a hyphen, period or forward slash. We can use a character class for this:
--- \b(\d{2})[-.\/]
Since we want to use the separator we matched here to match the same separator further into the date,
we're going to put it in a capturing group:
--- \b(\d{2})([-.\/])
• Next comes the month, which consists of a capital Latin letter and exactly two lowercase Latin letters:
--- \b(\d{2})([-.\/])([A-Z][a-z]{2})
•	Next, we're going to match the same separator we matched earlier. We can use a backreference for that:
--- \b(\d{2})([-.\/])([A-Z][a-z]{2})\2
•	Next up, we're going to match the year, which consists of exactly 4 digits:
--- \b(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})
•	Finally, since we don't want to match the date if there's anything else glued to it,
    we're going to use another word boundary for the end:
--- \b(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})\b
Now it's time to find all the valid dates in the input and print each date in the following format:
    "Day: {day}, Month: {month}, Year: {year}", each on a new line.
Examples:
    Input:
    13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016
    Output:
    Day: 13, Month: Jul, Year: 1928
    Day: 10, Month: Nov, Year: 1934
    Day: 25, Month: Dec, Year: 1937
"""

# This is the first approach, without naming the groups and then printing them using their group index:
"""
import re
pattern = r"(\d{2})([\.\-\/])([A-Z][a-z]{2})\2(\d{4})"
text = input()

matches = re.findall(pattern, text)

for day, separator, month, year in matches:
    print(f"Day: {day}, Month: {month}, Year: {year}")
"""

# And this is the second approach, and printing them using the group name:
# It's important to know: Reusing the name of the group inside the regex it's self is possible.
# To do so:
# - To create the group_with name: (?P<separator>[\.\-\/])
# - To reuse the group_with name: (?P=separator)
import re

pattern = r"(?P<day>\d{2})(?P<separator>[\.\-\/])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"

text = input()

matches = re.finditer(pattern, text)

for match in matches:
    day = match.group("day")
    separator = match.group("separator")
    month = match.group("month")
    year = match.group("year")
    print(f"Day: {day}, Month: {month}, Year: {year}")



