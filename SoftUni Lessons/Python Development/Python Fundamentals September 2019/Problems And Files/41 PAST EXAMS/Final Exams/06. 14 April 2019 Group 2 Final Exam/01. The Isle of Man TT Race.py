"""
Technology Fundamentals Final Exam - 14 April 2019 Group II
link: https://judge.softuni.bg/Contests/Practice/Index/1594#0
Name: 01. The Isle of Man TT Race
"""
import re

regex = r"(?P<tag>[\#\$\%\*\&])(?P<name>[a-zA-Z]+)(?P=tag)\=(?P<number>[0-9]+)\!\!(?P<message>.+)$"

while True:
    line = input()
    match = re.match(regex, line)
    if match:
        name = match.group("name")
        number = int(match.group("number"))
        message = match.group("message")
        if number == len(message):
            geo_hashcode = ""
            for symbol in message:
                geo_hashcode += chr(ord(symbol) + number)
            print(f"Coordinates found! {name} -> {geo_hashcode}")
            exit(0)
        else:
            print("Nothing found!")
    else:
        print("Nothing found!")
    if not line:
        break