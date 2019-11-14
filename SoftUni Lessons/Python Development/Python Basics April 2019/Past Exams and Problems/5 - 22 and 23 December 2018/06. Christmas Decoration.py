budget = int(input())

current_sum = 0

while True:
    decoration = input()
    if decoration == "Stop":
        break
    for letter in decoration:
        current_sum += ord(letter)
    if current_sum <= budget:
        print(f"Item successfully purchased!")
    else:
        print(f"Not enough money!")
        break

if decoration == "Stop":
    print(f"Money left: {budget - current_sum}")
