nums = [num for num in input().split()]
string = [letter for letter in input()]

key = ""

for num in nums:
    counter = sum([int(n) for n in num])
    index = counter % len(string)
    key += string[index]
    string.pop(index)

print(key)