"""
Programming Fundamentals Final Exam Preparation - 24 July 2019
link: https://judge.softuni.bg/Contests/Practice/Index/1759#1
Name: 02. Song Encryption
"""
import re

artist_regex = r"^[A-Z][a-z ']+$"
song_regex = r"^[A-Z ]+$"

while True:
    command = input()
    if command == "end":
        break
    artist = re.match(artist_regex, command.split(":")[0])
    song = re.match(song_regex, command.split(":")[1])
    if song and artist:
        key = len(artist.string)
        encryption = ""
        for letter in command:
            if letter == " " or letter == "'":
                encryption += letter
            elif letter == ":":
                encryption += "@"
            elif letter.islower():
                if ord(letter) + key <= 122:
                    encryption += chr(ord(letter) + key)
                else:
                    difference = (ord(letter) + key) - 122
                    new_letter = chr(96 + difference)
                    encryption += new_letter
            elif letter.isupper():
                if ord(letter) + key <= 90:
                    encryption += chr(ord(letter) + key)
                else:
                    difference = (ord(letter) + key) - 90
                    new_letter = chr(64 + difference)
                    encryption += new_letter
        print(f"Successful encryption: {encryption}")
    else:
        print("Invalid input!")
