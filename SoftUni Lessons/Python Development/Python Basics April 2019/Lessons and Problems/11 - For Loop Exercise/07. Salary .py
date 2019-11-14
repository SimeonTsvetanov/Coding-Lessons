tabs = int(input())
wage = int(input())

for i in range(0, tabs):
    website = input()
    if website == "Facebook":
        wage -= 150
    elif website == "Instagram":
        wage -= 100
    elif website == "Reddit":
        wage -= 50
    if wage <= 0:
        print("You have lost your salary.")
        break

if wage > 0:
    print(int(wage))
