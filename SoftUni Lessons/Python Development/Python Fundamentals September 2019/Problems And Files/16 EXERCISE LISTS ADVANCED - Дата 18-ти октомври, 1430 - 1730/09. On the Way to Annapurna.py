"""
Lists Advanced - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1731#7

SUPyF2 Lists-Advanced-Exercise - 09. On the Way to Annapurna (not included in final score)

Problem:
You’ve hired a Sherpa and he has a list of supplies you both need to go on the way.
He has passed you some notes and you have to order them correctly in a
diary before you start circling around the town’s stores.

Create a program, that lists stores and the items that can be found in them.
You are going to be receiving commands with the information you need until you get the "End" command.
There are three possible commands:
•	"Add->{Store}->{Item}"
o	Add the store and the item in your diary. If the store already exists, add just the item.
•	"Add->{Store}->{Item},{Item1}…,{ItemN}"
o	Add the store and the items to your notes. If the store already exists in the diary – add just the items to it.
•	"Remove->{Store}"
o	Remove the store and its items from your diary, if it exists.
In the end, print the collection sorted by the count of the items in descending order
and then by the names of the stores, again, in descending order in the following format:
Stores list:
{Store}
<<{Item}>>
<<{Item}>>
<<{Item}>>
Input / Constraints
•	You will be receiving information until the “END” command is given.
•	There will always be at least one store in the diary.
•	Input will always be valid, there is no need to check it explicitly.
Output
•	Print the list of stores in the format given above.

Examples:
Input:
Add->PeakSports->Map,Navigation,Compass
Add->Paragon->Sunscreen
Add->Groceries->Dried-fruit,Nuts
Add->Groceries->Nuts
Add->Paragon->Tent
Remove->Paragon
Add->Pharmacy->Pain-killers
END

Output:
Stores list:
PeakSports
<<Map>>
<<Navigation>>
<<Compass>>
Groceries
<<Dried-fruit>>
<<Nuts>>
<<Nuts>>
Pharmacy
<<Pain-killers>>

Comments:
First, we receive the "Add" command with a couple of items and we have to add the store and the items to.
We keep doing that for each line of input and when we receive the "Remove" command,
we delete the store and its items from our records.
In the end we print the stores sorted by the count of their items and then by their names.
"""
shops = []
while True:
    data = input().split("->")
    if data[0] == "END":
        break
    if data[0] == "Add":
        shop_in_list = False
        for shop in shops:
            if shop[0] == data[1]:
                shop += [item for item in data[2].split(",")]
                shop_in_list = True
                break
        if not shop_in_list:
            shops += [[data[1]] + [item for item in data[2].split(",")]]
    elif data[0] == "Remove":
        for shop in shops:
            if shop[0] == data[1]:
                shops.remove(shop)

shops = sorted(sorted(shops, key=lambda x: x[0], reverse=True), key=lambda x: len(x), reverse=True)

print(f"Stores list:")
for shop in shops:
    print(shop[0])
    for item in shop[1:]:
        print(f"<<{item}>>")

