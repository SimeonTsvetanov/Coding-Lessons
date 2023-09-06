a = [letter for letter in input()]
b = [letter for letter in input()]

for letter in range(len(b)):
    if a[letter] != b[letter]:
        a[letter] = b[letter]
        print("".join(a))
