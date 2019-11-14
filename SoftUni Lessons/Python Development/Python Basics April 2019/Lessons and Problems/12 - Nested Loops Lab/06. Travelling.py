destination = input()

while destination != "End":
    budget = float(input())
    save_money = 0
    while save_money < budget:
        save_money = save_money + float(input())
    print(f"Going to {destination}!")
    destination = input()
