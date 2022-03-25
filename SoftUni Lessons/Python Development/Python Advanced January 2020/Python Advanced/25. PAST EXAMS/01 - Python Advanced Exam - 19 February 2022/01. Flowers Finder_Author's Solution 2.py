from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())
words = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}
found_word = False

while vowels and consonants:
    v = vowels.popleft()
    c = consonants.pop()
    for word in words.keys():
        words[word] = words[word].replace(v, '')
        words[word] = words[word].replace(c, '')
        if words[word] == '':
            print(f"Word found: {word}")
            found_word = True
            break
    if found_word:
        break

if not found_word:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")

