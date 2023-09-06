words = [word.lower() for word in input().split(' ')]
print(*{word: words.count(word) for word in words if words.count(word) % 2 != 0}.keys())
