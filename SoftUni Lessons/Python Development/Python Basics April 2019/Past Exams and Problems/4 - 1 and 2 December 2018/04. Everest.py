command = input()

goal_height = 8848

count_days = 1
current_height = 5364

while command != "END":
    climbed_height = int(input())
    if command == "Yes":
        count_days += 1
    if count_days > 5:
        break
    current_height += climbed_height
    if current_height >= goal_height:
        break
    command = input()
if current_height >= goal_height:
    print(f"Goal reached for {count_days} days!")
else:
    print(f"Failed!\n{current_height}")
