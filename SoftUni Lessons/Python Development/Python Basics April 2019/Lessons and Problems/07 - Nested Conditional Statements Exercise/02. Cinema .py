type_move = input()
r = int(input())
c = int(input())

total_seats = r * c
price = 0

if type_move == "Premiere":
    price = 12.00 * total_seats
elif type_move == "Normal":
    price = 7.50 * total_seats
elif type_move == "Discount":
    price = 5.00 * total_seats

print(f"{price:.2f} leva")
