letters_set = set()
text = input()

for letter in text:
    letters_set.add(letter)

for letter in sorted(letters_set):
    print(f"{letter}: {text.count(letter)} time/s")
