budget = float(input())

name = None

while True:
    if budget <= 0:
        break
    name = input()
    if name == "ACTION":
        break
    if len(name) > 15:
        budget -= budget * 0.2
    else:
        wage = float(input())
        budget -= wage

if budget >= 0:
    print(f"We are left with {budget:.2f} leva.")
else:
    print(f"We need {abs(budget):.2f} leva for our actors.")
