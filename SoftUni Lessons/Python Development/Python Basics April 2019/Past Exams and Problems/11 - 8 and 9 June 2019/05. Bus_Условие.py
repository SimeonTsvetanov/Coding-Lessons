count_travellers = int(input())
count_stops = int(input())

for stop in range(1, count_stops + 1):
    going_out_travelers = int(input())
    count_travellers -= going_out_travelers
    going_in_travelers = int(input())
    count_travellers += going_in_travelers
    if stop % 2 != 0:
        count_travellers += 2
    elif stop % 2 == 0:
        count_travellers -= 2

print(f"The final number of passengers is : {count_travellers}")
