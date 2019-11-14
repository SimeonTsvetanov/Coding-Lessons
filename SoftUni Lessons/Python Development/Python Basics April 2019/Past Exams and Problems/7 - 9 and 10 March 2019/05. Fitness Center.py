people = int(input())

count_back = 0
count_chest = 0
count_legs = 0
count_abs = 0
count_protein_shake = 0
count_protein_bar = 0

count_workout = 0
count_protein_use = 0

for i in range(people):
    command = input()
    if command == "Back":
        count_back += 1
        count_workout += 1
    elif command == "Chest":
        count_chest += 1
        count_workout += 1
    elif command == "Legs":
        count_legs += 1
        count_workout += 1
    elif command == "Abs":
        count_abs += 1
        count_workout += 1
    elif command == "Protein shake":
        count_protein_shake += 1
        count_protein_use += 1
    elif command == "Protein bar":
        count_protein_bar += 1
        count_protein_use += 1

print(f"{count_back} - back")
print(f"{count_chest} - chest")
print(f"{count_legs} - legs")
print(f"{count_abs} - abs")
print(f"{count_protein_shake} - protein shake")
print(f"{count_protein_bar} - protein bar")
print(f"{(count_workout / people * 100):.2f}% - work out")
print(f"{(count_protein_use / people * 100):.2f}% - protein")
