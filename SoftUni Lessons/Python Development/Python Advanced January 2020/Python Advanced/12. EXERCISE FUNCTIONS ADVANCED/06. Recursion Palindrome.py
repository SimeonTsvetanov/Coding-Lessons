def palindrome(text, idx):
    """This is the solution from work in class
    We need to check if the word, given is palindrome or not:"""
    second_idx = len(text) - 1 - idx
    if idx == len(text) // 2:
        return f"{text} is a palindrome"
    if text[idx] == text[second_idx]:
        return palindrome(text, idx + 1)
    else:
        return f"{text} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
