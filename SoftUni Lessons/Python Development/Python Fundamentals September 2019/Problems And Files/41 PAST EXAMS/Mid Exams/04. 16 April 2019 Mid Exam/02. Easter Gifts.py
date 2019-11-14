"""
Technology Fundamentals Retake Mid Exam - 16 April 2019
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1610#1

SUPyF2 P.-Mid-Exam/16 April 2019 - 02. Easter Gifts

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
StuffedAnimal Spoon Sweets EasterBunny ChocolateEgg

Comments:
First, we receive the command "OutOfStock" and we need to replace the values of "Eggs" with "None".  After this command the list should look like this:
None StuffedAnimal Cozonac Sweets EasterBunny None Clothes.
Afterwards, we receive the "Required" command and we need to replace the value on the 2nd index of our list with the value "Spoon". The list should look like this:
None StuffedAnimal Spoon Sweets EasterBunny None Clothes
After, we receive the "JustInCase" command, which means we need to replace the last value in our list with "ChocolateEggs". The list should look like this:
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
gifts = input().split()

while True:
    command = input().split()
    if command[0] == "No":
        print(' '.join(gift for gift in gifts if gift != "None"))
        break

    elif command[0] == "OutOfStock":
        gift_to_delete = command[1]
        gifts = ["None" if gift == gift_to_delete else gift for gift in gifts]

    elif command[0] == "Required":
        new_gift, index = command[1], int(command[2])
        if 0 <= index < len(gifts):
            gifts[index] = new_gift

    elif command[0] == "JustInCase":
        new_last_gift = command[1]
        gifts[-1] = new_last_gift

