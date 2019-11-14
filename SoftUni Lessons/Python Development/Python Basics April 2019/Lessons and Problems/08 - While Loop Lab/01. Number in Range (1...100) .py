num = int(input())

while num < 1 or num > 100:
    print("Invalid number!")
    num = int(input())

print(f"The number is: {num}.")
