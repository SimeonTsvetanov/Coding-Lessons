bought_food = int(input()) * 1000
command = None

while command != "Adopted":
    command = input()
    if command == "Adopted":
        break
    bought_food -= int(command)

if bought_food >= 0:
    print(f"Food is enough! Leftovers: {bought_food} grams.")
else:
    print(f"Food is not enough. You need {abs(bought_food)} grams more.")
