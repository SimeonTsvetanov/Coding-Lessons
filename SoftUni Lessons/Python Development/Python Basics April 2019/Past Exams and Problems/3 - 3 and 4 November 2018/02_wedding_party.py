people = int(input())
budget = int(input())

price = people * 20

if price > budget:
    print(f"They won't have enough money to pay the covert. They will need {price - budget} lv more.")
else:
    difference = budget - price
    fireworks_money = difference * 0.4
    leftover_money = difference * 0.6
    print(f"Yes! {int(fireworks_money)} lv are for fireworks and {round(leftover_money)} lv are for donation.")
