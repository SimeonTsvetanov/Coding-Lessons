"""
Programming Fundamentals Final Exam - 03 August 2019 Group 2
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1749#1
Name: Message Encrypter
"""
import re
regex = r"(?P<startEnd>(\*|@))(?P<tag>[A-Z][a-z][a-z]+)(?P=startEnd):[ ]\[(?P<first>[A-Za-z])\]\|\[(?P<second>[a-zA-Z])\]\|\[(?P<third>[a-zA-Z])\]\|$"

for each_time in range(int(input())):
    message = input()
    match = re.search(regex, message)
    if match:
        tag = match.group("tag")
        first = ord(match.group("first"))
        second = ord(match.group("second"))
        third = ord(match.group("third"))
        print(f"{tag}: {first} {second} {third}")
    else:
        print(f"Valid message not found!")
