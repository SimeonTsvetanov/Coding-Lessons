string = input()

capital_letter_indices = []

for i in range(len(string)):
    if string[i].isupper():
        capital_letter_indices.append(i)

print(capital_letter_indices)
