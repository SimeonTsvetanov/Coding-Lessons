text = input()

letters = {letter: text.count(letter) for letter in text if letter != ' '}

{(print(f"{letter} -> {text}")) for (letter, text) in letters.items()}
