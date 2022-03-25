flowers = ["rose", "tulip", "lotus", "daffodil"]

vowels = input().split()
consonants = input().split()
collected = []
found = ''

while True:
    if len(vowels) == 0 or len(consonants) == 0 or found:
        break
    v = vowels[0]
    c = consonants[-1]
    vowels.remove(vowels[0])
    consonants.remove(consonants[-1])

    collected.append(v)
    collected.append(c)
    for flower in flowers:
        flower_letters = [li for li in flower]
        check = all(item in collected for item in flower_letters)
        if check:
            found = flower
            break

if found:
    print(f"Word found: {found}")
else:
    print(f"Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")


