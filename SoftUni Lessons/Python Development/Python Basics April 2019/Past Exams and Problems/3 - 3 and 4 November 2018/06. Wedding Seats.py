last_sector = ord(input())
count_rows_first_sector = int(input())
count_seats_odd = int(input())

count_seats_even = count_seats_odd * 2
total_seats_sector = count_seats_odd + count_seats_even
total = 0

for sector in range(65, last_sector + 1):
    for j in range(1, count_rows_first_sector + 1):
        if j % 2 == 1:
            for k in range(count_seats_odd):
                print(f"{chr(sector)}{j}{chr(k + 97)}")
                total += 1
        elif j % 2 == 0:
            for k in range(count_seats_odd + 2):
                print(f"{chr(sector)}{j}{chr(k + 97)}")
                total += 1
    count_rows_first_sector += 1
print(total)

