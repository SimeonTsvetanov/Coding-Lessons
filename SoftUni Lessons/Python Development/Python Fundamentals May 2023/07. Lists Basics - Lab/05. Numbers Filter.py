# On the first line, you will receive a single number n.
n = int(input())

# On the following n lines, you will receive integers.
integers = [int(input()) for _ in range(n)]

# After that, you will be given one of the following commands:
# • even
# • odd
# • negative
# • positive
# Filter all the numbers that fit in the category (0 counts as a positive and even)
command = input()
filtered = []

if command == 'even':
    filtered = [num for num in integers if num % 2 == 0]
if command == 'odd':
    filtered = [num for num in integers if num % 2 != 0]
if command == 'negative':
    filtered = [num for num in integers if num < 0]
if command == 'positive':
    filtered = [num for num in integers if num >= 0]

# Finally, print the result.
print(filtered)
