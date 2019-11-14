"""
Dictionaries - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1736#4

SUPyF2 Dictionaries-Lab - 05. Word Synonyms

Problem:
Write a program, which keeps a dictionary with synonyms.
The key of the dictionary will be the word.
The value will be a list of all the synonyms of that word.
You will be given a number n – the count of the words.
After each word, you will be given a synonym,
so the count of lines you have to read from the console is 2 * n.
You will be receiving a word and a synonym each on a separate line like this:
•	{word}
•	{synonym}
If you get the same word twice, just add the new synonym to the list.
Print the words in the following format:
{word} - {synonym1, synonym2… synonymN}
Examples:
Input:
3
cute
adorable
cute
charming
smart
clever

Output:
cute - adorable, charming
smart - clever

Input:
2
task
problem
task
assignment

Output:
task – problem, assignment
"""
times = int(input())
synonyms = {}

for how_ever_many_times in range(times):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = [synonym]
    else:
        synonyms[word].append(synonym)

for word in synonyms:
    print(F"{word} - {', '.join(synonyms[word])}")
