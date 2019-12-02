"""
Technology Fundamentals Retake Final Exam - 18 April 2018
link: https://judge.softuni.bg/Contests/Practice/Index/1612#0
Name: 01. Animal Sanctuary
"""

import re
regex_full_message = r"^[n]:(?P<name>[^\;;]+)\;t:(?P<kind>[^\;;]+)\;c\-\-(?P<country>[A-Za-z ]+)$"
total_weight = 0

for each_time in range(int(input())):
    message = input()
    match = re.match(regex_full_message, message)
    if match:
        name_coded = match.group("name")
        kind_coded = match.group("kind")
        country_coded = match.group("country")
        name = ""
        kind = ""
        country = ""

        for symbol in name_coded:
            if symbol.isalpha() or symbol == " ":
                name += symbol
            elif symbol.isdigit():
                total_weight += int(symbol)

        for symbol in kind_coded:
            if symbol.isalpha() or symbol == " ":
                kind += symbol
            elif symbol.isdigit():
                total_weight += int(symbol)

        for symbol in country_coded:
            if symbol.isalpha() or symbol == " ":
                country += symbol
            elif symbol.isdigit():
                total_weight += int(symbol)

        print(f"{name} is a {kind} from {country}")

print(f"Total weight of animals: {total_weight}KG")
