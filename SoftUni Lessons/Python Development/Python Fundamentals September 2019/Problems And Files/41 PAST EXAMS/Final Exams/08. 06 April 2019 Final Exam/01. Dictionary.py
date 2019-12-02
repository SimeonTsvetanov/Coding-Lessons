"""
(Demo) Technology Fundamentals Final Exam - 06 April 2019
link: https://judge.softuni.bg/Contests/Practice/Index/1628#0
Name: 01. Arriving in Kathmandu
"""
dictionary = {}

all_words = input().split(" | ")
for word_and_definition in all_words:
    word = word_and_definition.split(": ")[0]
    definition = word_and_definition.split(": ")[1]
    if word not in dictionary:
        dictionary[word] = [definition]
    else:
        dictionary[word] += [definition]

words = input().split(" | ")
for word in words:
    if word in dictionary:
        print(f"{word}")
        for definition in sorted(dictionary[word], key=lambda x: -len(x)):
            print(f" -{definition}")

command = input()
if command == "End":
    exit(0)
elif command == "List":
    for word in sorted(dictionary):
        print(word, end=" ")
