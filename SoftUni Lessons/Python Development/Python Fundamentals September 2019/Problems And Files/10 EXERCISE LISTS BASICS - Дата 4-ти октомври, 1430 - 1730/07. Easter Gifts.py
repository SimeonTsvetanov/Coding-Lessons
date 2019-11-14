"""
Lists Basics - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1725#6

SUPyF2 Lists Basics Exercise - 07. Easter Gifts (not included in final score)

Problem:
As a good friend, you decide to buy presents for your friends.
Create a program that helps you plan the gifts for your friends and family.
First, you are going to receive the gifts you plan on buying оn a single line,
separated by space, in the following format:
"{gift1} {gift2} {gift3}… {giftn}"
Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
•	"OutOfStock {gift}"
o	Find the gifts with this name in your collection, if there are any, and change their values to "None".
•	"Required {gift} {index}"
o	Replace the value of the current gift on the given index with this gift, if the index is valid.
•	"JustInCase {gift}"
o	Replace the value of your last gift with this one.
In the end, print the gifts on a single line, except the ones with value "None",
separated by a single space in the following format:
"{gift1} {gift2} {gift3}… {giftn}"
Input / Constraints
•	On the 1st line you are going to receive the names of the gifts, separated by a single space.
•	On the next lines, until the "No Money" command is received, you will be receiving commands.
•	The input will always be valid.
Output
•	Print the gifts in the format described above.

Examples:

Input:
Eggs StuffedAnimal Cozonac Sweets EasterBunny Eggs Clothes
OutOfStock Eggs
Required Spoon 2
JustInCase ChocolateEgg
No Money

Output:
Eggs StuffedAnimal Cozonac Sweets EasterBunny Eggs Clothes
OutOfStock Eggs
Required Spoon 2
JustInCase ChocolateEgg
No Money	StuffedAnimal Spoon Sweets EasterBunny ChocolateEgg

Comments:
First, we receive the command "OutOfStock" and we need to replace the values of "Eggs" with "None".
After this command the list should look like this:
None StuffedAnimal Cozonac Sweets EasterBunny None Clothes.
Afterwards, we receive the "Required" command and we need to replace the value on the 2nd index of our list with the
value "Spoon". The list should look like this:
None StuffedAnimal Spoon Sweets EasterBunny None Clothes
After, we receive the "JustInCase" command, which means we need to replace the last value in our
list with "ChocolateEggs". The list should look like this:
None StuffedAnimal Spoon Sweets EasterBunny None ChocolateEggs
In the end, we print all of the gifts, except the ones with values "None". This is the result list:
StuffedAnimal Spoon Sweets EasterBunny ChocolateEggs

Input:
Sweets Cozonac Clothes Flowers Wine Clothes Eggs Clothes
Required Paper 8
OutOfStock Clothes
Required Chocolate 2
JustInCase Hat
OutOfStock Cable
No Money

Output:
Sweets Cozonac Chocolate Flowers Wine Eggs Hat
"""
gifts = [gift for gift in input().split()]

while True:
    command = input()
    if command == "No Money":
        break
    command = [item for item in command.split()]
    if command[0] == "OutOfStock":
        for gift in gifts:
            if gift == command[1]:
                index_to_change = gifts.index(gift)
                gifts.pop(index_to_change)
                gifts.insert(index_to_change, "None")
    elif command[0] == "Required":
        if 0 <= int(command[2]) <= len(gifts) - 1:
            gifts.pop(int(command[2]))
            gifts.insert(int(command[2]), command[1])
    elif command[0] == "JustInCase":
        gifts.pop(-1)
        gifts.append(command[1])

print(" ".join([gift for gift in gifts if gift != "None"]))


