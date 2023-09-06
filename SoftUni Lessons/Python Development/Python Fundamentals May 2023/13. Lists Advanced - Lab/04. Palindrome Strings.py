words = [word for word in input().split()]
palindrome = input()

print([word for word in words if word == word[::-1]])
print(f"Found palindrome {words.count(palindrome)} times")
