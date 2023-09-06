result = 'All numbers are even.'

for i in range(int(input())):
    num = int(input())
    if num % 2 != 0:
        result = f"{num} is odd!"
        break

print(result)
