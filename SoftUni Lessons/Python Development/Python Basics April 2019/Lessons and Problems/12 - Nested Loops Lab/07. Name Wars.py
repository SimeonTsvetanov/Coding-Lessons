max_sum = 0
name_max_sum = None

while True:
    command = input()
    if command == "STOP":
        break
    current_sum = 0
    for i in command:
        current_sum += ord(i)
    if current_sum > max_sum:
        max_sum = current_sum
        name_max_sum = command

print(f"Winner is {name_max_sum} - {max_sum}!")


