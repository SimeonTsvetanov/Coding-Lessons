import math

aim_money = float(input())
count_fantasy_books = int(input())
count_horror_books = int(input())
count_romantic_books = int(input())

total_sale = (count_fantasy_books * 14.9) + (count_horror_books * 9.8) + (count_romantic_books * 4.30)
total_sale -= total_sale * 0.2

if total_sale < aim_money:
    print(f"{abs(total_sale - aim_money):.2f} money needed.")

for_salesman = 0
remaining = 0
difference = total_sale - aim_money

if total_sale > aim_money:
    for_salesman = math.floor(difference * 0.1)
    remaining = difference - for_salesman
    total_gift = aim_money + remaining
    print(f"{total_gift:.2f} leva donated.")
    print(f"Sellers will receive {for_salesman} leva.")

