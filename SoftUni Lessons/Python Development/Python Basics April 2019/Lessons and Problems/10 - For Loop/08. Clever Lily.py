lily_age = int(input())
washing_machine_price = float(input())
one_toy_price = float(input())

birthday_money = 0
toys = 0

for i in range(1, lily_age + 1):
    if i % 2 != 0:
        toys += 1
    else:
        birthday_money += i * 5
        birthday_money -= 1

toys_money = toys * one_toy_price
saved_money = birthday_money + toys_money


if saved_money >= washing_machine_price:
    print(f"Yes! {abs(saved_money - washing_machine_price):.2f}")
else:
    print(f"No! {abs(washing_machine_price - saved_money):.2f}")

