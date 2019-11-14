start_interval = int(input())
end_interval = int(input())
magic_number = int(input())

checker = False
checked_combinations = 0

for num_1 in range(start_interval, end_interval + 1):
    if checker:
        break
    for num_2 in range(start_interval, end_interval + 1):
        checked_combinations += 1
        if num_1 + num_2 == magic_number:
            print(f"Combination N:{checked_combinations} ({num_1} + {num_2} = {magic_number})")
            checker = True
            break
if not checker:
    print(f"{checked_combinations} combinations - neither equals {magic_number}")
