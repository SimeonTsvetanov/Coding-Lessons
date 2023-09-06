words = {}

for i in range(int(input())):
    word, synonym = input(), input()
    if word not in words:
        words[word] = []
    words[word].append(synonym)

for word, synonyms in words.items():
    print(f"{word} - {', '.join(synonyms)}")
