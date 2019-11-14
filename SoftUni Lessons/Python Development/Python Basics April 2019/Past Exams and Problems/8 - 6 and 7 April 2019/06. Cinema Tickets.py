movie_name = None
free_spaces = 0
type_ticket = None
student = 0
standard = 0
kid = 0
total_sold = 0
current_move_total = 0

while True:
    movie_name = input()
    if movie_name == "Finish":
        break
    free_spaces = int(input())
    while True:
        if current_move_total == free_spaces:
            break
        type_ticket = input()
        if type_ticket == "End":
            break
        if type_ticket == "student":
            student += 1
            total_sold += 1
            current_move_total += 1
        elif type_ticket == "standard":
            standard += 1
            total_sold += 1
            current_move_total += 1
        elif type_ticket == "kid":
            kid += 1
            total_sold += 1
            current_move_total += 1
    print(f"{movie_name} - {(current_move_total / free_spaces * 100):.2f}% full.")
    current_move_total = 0

print(f"Total tickets: {total_sold}")
print(f"{(student / total_sold * 100):.2f}% student tickets.")
print(f"{(standard / total_sold * 100):.2f}% standard tickets.")
print(f"{(kid / total_sold * 100):.2f}% kids tickets.")
