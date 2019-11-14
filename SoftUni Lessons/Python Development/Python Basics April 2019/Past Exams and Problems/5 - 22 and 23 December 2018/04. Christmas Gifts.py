under_16 = 0
over_16 = 0

toys_total = 0
pullovers_total = 0

command = None

while command != "Christmas":
    command = input()
    if command == "Christmas":
        break
    if int(command) <= 16:
        under_16 += 1
        toys_total += 5
    elif int(command) > 16:
        over_16 += 1
        pullovers_total += 15

print(f"Number of adults: {over_16}")
print(f"Number of kids: {under_16}")
print(f"Money for toys: {toys_total}")
print(f"Money for sweaters: {pullovers_total}")

