"""
Text Processing - More Exercises
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1741#3

SUPyF2 Text-Pr.-More-Ex. - 04. Morse Code Translator

Problem:
Write a program that translates messages from Morse code to English (capital letters).
Use this page to help you (without the numbers). The words will be separated by a space (' '). There will be a '|'
character which you should replace with ' ' (space).
Example:
Input:
.. | -- .- -.. . |  -.-- --- ..- | .-- .-. .. - . | .- | .-.. --- -. --. | -.-. --- -.. .
Output:
I MADE YOU WRITE A LONG CODE
Input:
.. | .... --- .--. . | -.-- --- ..- | .- .-. . | -. --- - | -- .- -..
Output:
I HOPE YOU ARE NOT MAD

#TODO This task is SOLVED, but Judge doesn't support a check with Python for now,
"""
morse_code_dict = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
}
code = input().split()
decrypted_code = ""
for letter in code:
    if letter == "|":
        decrypted_code += " "
    else:
        for key, value in morse_code_dict.items():
            if letter == value:
                decrypted_code += key
print(decrypted_code)
