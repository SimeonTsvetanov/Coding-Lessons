count_easter_bread = int(input())
name_backer = None
current_score = 0
max_score = 0

max_score_name = None

for i in range(1, count_easter_bread + 1):
    name_backer = input()
    while True:
        command = input()
        if command == "Stop":
            break
        current_score += int(command)
    print(f"{name_backer} has {current_score} points.")
    if current_score > max_score:
        print(f"{name_backer} is the new number 1!")
        max_score = current_score
        max_score_name = name_backer
    current_score = 0

print(f"{max_score_name} won competition with {max_score} points!")
