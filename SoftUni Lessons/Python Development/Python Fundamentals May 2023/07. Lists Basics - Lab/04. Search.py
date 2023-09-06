# On the first line, you will receive a number n
n = int(input())

# On the second line, you will receive a word
word = input()

# On the following n lines,
# you will be given some strings. You should add them to a list and print them.
strings = []
[strings.append(input()) for _ in range(n)]
print(strings)

# After that, you should filter out only
# the strings that include the given word and print that list too.
filtered = list(filter(lambda string: word in string, strings))
print(filtered)
