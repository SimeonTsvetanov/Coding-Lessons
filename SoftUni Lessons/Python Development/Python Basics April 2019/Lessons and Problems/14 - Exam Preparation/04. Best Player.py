name = None
max_goals = 0
max_name = None
trick = None

while True:
    name = input()
    if name == "END":
        break
    goals = int(input())
    if goals > max_goals:
        max_goals = goals
        max_name = name
    if goals >= 3:
        trick = "yes"
    if goals >= 10:
        break

print(f"{max_name} is the best player!")
if trick == "yes":
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")
