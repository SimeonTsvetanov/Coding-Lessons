while True:
    word = input()
    if word == "End":
        break
    if word == "SoftUni":
        continue
    print(''.join([letter * 2 for letter in word]))
