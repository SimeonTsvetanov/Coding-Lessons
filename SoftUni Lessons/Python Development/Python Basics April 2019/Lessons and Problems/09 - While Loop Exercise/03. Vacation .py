needed_money = float(input())
owned_money = float(input())

total_days = 0
days_spend = 0

while owned_money < needed_money and days_spend != 5:
    command = input()
    money = float(input())
    total_days += 1
    if command == "save":
        owned_money += money
        days_spend = 0
    elif command == "spend":
        owned_money -= money
        days_spend += 1
        if owned_money < 0:
            owned_money = 0

if days_spend == 5:
    print("You can't save the money.")
    print(total_days)
if owned_money >= needed_money:
    print(f"You saved the money for {total_days} days.")
