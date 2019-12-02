"""
Technology Fundamentals Final Exam - 14 April 2019 Group I
link: https://judge.softuni.bg/Contests/Practice/Index/1516#0
Name: 01. Arriving in Kathmandu
"""
import re

pattern = r"^(?P<name>[A-Za-z0-9\!@#\$\?]+)\=(?P<length>[0-9]+)<<(?P<geohash>.+)$"

while True:
    line = input()
    if line == "Last note":
        break
    match = re.match(pattern, line)
    if match and len(match.group("geohash")) == int(match.group("length")):
        name = ''.join([letter for letter in match.group("name") if letter.isalpha()])
        print(f"Coordinates found! {name} -> {match.group('geohash')}")
    else:
        print(f"Nothing found!")

