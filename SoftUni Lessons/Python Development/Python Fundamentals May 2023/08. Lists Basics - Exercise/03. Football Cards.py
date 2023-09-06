cards = [card for card in input().split(' ')]

a = []
b = []

terminated = False

for card in cards:
    if "A" in card and card not in a:
        a.append(card)
    elif "B" in card and card not in b:
        b.append(card)

    if len(a) >= 5 or len(b) >= 5:
        terminated = "Game was terminated"
        break


print(f"Team A - {11 - len(a)}; Team B - {11 - len(b)}")
if terminated:
    print(terminated)
