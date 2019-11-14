"""
Lists
Check your answer: https://judge.softuni.bg/Contests/Practice/Index/1087#1

02. Split by Word Casing

Problem:
Read a text, split it into words and distribute them into 3 lists.
- Lower-case words like “programming”, “at” and “databases” – consist of lowercase letters only.
- Upper-case words like “PHP”, “JS” and “SQL” – consist of uppercase letters only.
- Mixed-case words like “C#”, “SoftUni” and “Java” – all others.
Use the following separators between the words: , ; : . ! ( ) " ' \ / [ ] space
Print the 3 lists as shown in the example below.

Examples
Input:
Learn programming at SoftUni: Java, PHP, JS, HTML 5, CSS, Web, C#, SQL, databases, AJAX, etc.

Output:
Lower-case: programming, at, databases, etc
Mixed-case: Learn, SoftUni, Java, 5, Web, C#
Upper-case: PHP, JS, HTML, CSS, SQL, AJAX

Hints
- Split the input text using the above described separators.
- Process the obtained list of words one by one.
- Create 3 lists of words: lowercase words, mixed-case words and uppercase words.
- Check each word and append it to one of the above 3 lists:
- Count the lowercase letters and uppercase letters.
- If all letters are lowercase, append the word to the lowercase list.
- If all letters are uppercase, append the word to the uppercase list.
- Otherwise the word is considered mixed-case  append it to the mixed-case list.
- Print the obtained 3 lists as shown in the example above.
"""
import re
words = [str(item) for item in re.split("[,;:.!()\"\'\\\\/\[\] ]+", input())if item != ""]

lower_case = []
upper_case = []
mixed_case = []

for word in words:
    if word.islower():
        checker = True
        for letter in word:
            if 97 <= ord(letter) <= 122:
                checker = True
            else:
                checker = False
                break
        if checker:
            lower_case += [word]
        else:
            mixed_case += [word]

    elif word.isupper():
        checker = True
        for letter in word:
            if 65 <= ord(letter) <= 90:
                checker = True
            else:
                checker = False
                break
        if checker:
            upper_case += [word]
        else:
            mixed_case += [word]
    else:
        mixed_case += [word]

print(f"Lower-case: ", end="")
print(", ".join(lower_case))
print(f"Mixed-case: ", end="")
print(", ".join(mixed_case))
print(f"Upper-case: ", end="")
print(", ".join(upper_case))
