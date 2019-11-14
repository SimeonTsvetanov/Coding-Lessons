count_fish = int(input())

total_amount = 0
current_total = 0
counter = 0
catch = 0

while True:
    name_fish = input()
    if name_fish == "Stop":
        break
    counter += 1
    count_fish -= 1
    catch += 1
    fish_weight = float(input())
    for i in name_fish:
        letter_to_num = ord(i)
        current_total += letter_to_num
    if counter == 3:
        total_amount += current_total / fish_weight
        counter = 0
    else:
        total_amount -= current_total / fish_weight
    current_total = 0
    if count_fish == 0:
        break

if count_fish <= 0:
    print("Lyubo fulfilled the quota!")
if total_amount >= 0:
    print(f"Lyubo's profit from {catch} fishes is {total_amount:.2f} leva.")
else:
    print(f"Lyubo lost {abs(total_amount):.2f} leva today.")


