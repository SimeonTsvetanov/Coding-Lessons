width = int(input())
length = int(input())

size_cake = width * length
sum_parts = 0

while True:
    command = input()
    if command == "STOP":
        break
    part = int(command)
    sum_parts += part
    if size_cake < sum_parts:
        break

if size_cake < sum_parts:
    print(f"No more cake left! You need {sum_parts - size_cake} pieces more.")
else:
    print(f"{size_cake - sum_parts} pieces are left.")
