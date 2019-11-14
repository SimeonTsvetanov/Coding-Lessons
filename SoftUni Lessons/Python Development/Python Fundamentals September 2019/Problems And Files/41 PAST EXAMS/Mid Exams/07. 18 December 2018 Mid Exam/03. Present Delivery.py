"""
Technology Fundamentals Retake Mid Exam - 18 December 2018
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1395#2

SUPyF2 P.-Mid-Exam/18 December 2018 - 03. Present Delivery

Problem:
Santa has limited time to drop at least some presents for each house. Help him with his mission!
You will receive a string with even integers separated by "@" representing each house with its
number of members and a series of Jump commands until you receive "Merry Xmas!"
Santa starts at the position of the first house and has to jump by a given length.
The jump command will be in format: "Jump {length}".
Each time he jumps from one house to another he drops 2 presents for that house and decreases the needed presents
for that house. If Santa jumps on a house which doesn't need more presents (presents = 0) you should instead print
"House {houseIndex} will have a Merry Christmas.".
Keep in mind that Santa can have a bigger jump length than the size of the field and if he does jump outside
of it he should start from the beginning again.
For example we have a field of size 3 and each house has 6 members. Santa is at the start and jumps with length of 2.
He will end up at index 2 and decrease the needed presents by 2 (6 – 2 = 4).
Next he jumps again with length of 2 and ends up at index position 1 and again decreases the needed presents.

Input
•	On the first line you will receive a string with even integers separated by "@" – houses and their number of members
•	On the next lines until "Merry Xmas!" you will receive jump commands in format: "Jump {length}".
Output
At the end print Santa's last position and whether or not his mission was successful:
•	"Santa's last position was {lastPositionIndex}."
•	If all members of each house have presents print:
o	"Mission was successful."
•	If not print the count of all houses that won't have a Merry Christmas:
o	"Santa has failed {housesCount} houses."
Constraints
•	The field can be of size [1…20]
•	Each house will have an even number of  members [2 … 10]
•	Each jump length will be an integer [1 … 20]
 
Examples:

Input:          Output:
10@10@10@2      Santa's last position was 3.
Jump 1          Santa has failed 3 houses.
Jump 2
Merry Xmas!

Input:          Output:
2@4@2           House 0 will have a Merry Christmas.
Jump 2          Santa's last position was 1.
Jump 2          Mission was successful.
Jump 8
Jump 3
Jump 1
Merry Xmas!
"""
houses = [int(house) for house in input().split("@")]
santa_position = 0

while True:
    command = input().split()
    if command[0] == "Merry":
        break
    jump = int(command[1])

    if santa_position + jump >= len(houses):
        santa_position = (santa_position + jump) % len(houses)
    else:
        santa_position = santa_position + jump

    if houses[santa_position] == 0:
        print(f"House {santa_position} will have a Merry Christmas.")
    else:
        houses[santa_position] -= 2


print(f"Santa's last position was {santa_position}.")
if sum(houses) == 0:
    print(f"Mission was successful.")
else:
    print(f"Santa has failed {len([house for house in houses if house > 0])} houses.")




