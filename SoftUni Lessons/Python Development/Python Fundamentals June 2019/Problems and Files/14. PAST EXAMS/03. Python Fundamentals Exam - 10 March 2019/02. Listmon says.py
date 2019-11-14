"""
Basics OOP Principles
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/1511#1

SUPyF Exam 10.03.2019 - 02. Listmon says

Problem:
Input / Constraints
We are at the Listmon's playground. The collection defines its own rules and if we want to beat It in its own game,
we must play by the rules .A game is pretty similar to 'Simon says'.
So, It will tell us what to do and we should read very carefully what It wants from us.
At the beginning of the game Listmon will give us an input with different elements separated by space (one or several).
The elements will be numbers.
After that It will start giving us commands in format:
•	set
•	filter {command} (where command will be either odd or even)
•	multiply {number}
•	divide {number}
•	slice {indexN} {indexM}
•	sort
•	reverse

*If you receive command 'set' you should check if the list is not already with unique elements, if this is so -
print:
•	"It is a set"
If it isn't, make it one and print it as a list.
Keep the order of the elements exactly the same as Listmon gave it to you, just remove the non-unique elements.
*If you receive ‘filter’ you should print only either odds elements, or even, depending on the command next to filter.
If there are no elements in the list after filter command do not print the list.
*If you receive 'multiply', multiply every element of the list by the given number.
*If you receive ‘divide’ you must divide every element by the given number and print the list. If the number is 0, print
•	'ZeroDivisionError caught'  And do not print the list.
*If you receive ‘slice’ {indexN} {indexM} you should print the elements from n to m including without actually
changing the list! Keep in mind that Listmon is tricky and can give you indexes which are not part of the list.
In this case you should print:
•	'IndexError caught '.
And do not print the list.
Index N always will be smaller number than M if the two indexes are valid
*If you receive sort - print the elements in ascending order.
*If you receive reverse – print all elements in reversed order.

ALWAYS keep in mind that the Listmon’s list never should be changed, otherwise we are going to lose the game.

NOTE:
 After each command you should print the result ONLY if there are elements in the list.
 If the list is empty do not print it!
Output
When you recieve a commant which says 'exhausted', you should print the count of roundes played in format:
•	"I beat It for {count} rounds!"
where count is the number of commands you have recieved during the game.

Examples:

Input:
1 3 2 4 5
set
slice 1 5
sort
reverse
exhausted

Output:
It is a set
IndexError caught
[1, 2, 3, 4, 5]
[5, 4, 2, 3, 1]
I beat It for 4 rounds!

Input:
1 15 3 279 12
filter odd
multiply 7
divide 0
reverse
exhausted

Output:
[1, 15, 3, 279]
[7, 105, 21, 1953, 84]
ZeroDivisionError caught
[12, 279, 3, 15, 1]
I beat It for 4 rounds!
"""

nums = [int(item) for item in input().split(" ") if item != ""]
count_rounds = 0
while True:
    command = input()
    if command == "exhausted":
        break

    elif command == "set":
        count_rounds += 1
        unique = len(set(nums)) == len(nums)
        if unique:
            print("It is a set")
        else:
            unique_leftovers = []
            for num in nums:
                if num not in unique_leftovers:
                    unique_leftovers += [int(num)]
            print(unique_leftovers)

    elif "filter" in command:
        count_rounds += 1
        if "even" in command:
            even = [item for item in nums if item % 2 == 0]
            if even:
                print(even)
        elif "odd" in command:
            odd = [item for item in nums if item % 2 != 0]
            if odd:
                print(odd)

    elif "multiply" in command:
        count_rounds += 1
        split_the_command = [item for item in command.split(" ")]
        multiply_by = int(split_the_command[1])
        multiplied_nums = [int(num) * multiply_by for num in nums]
        print(multiplied_nums)

    elif "divide" in command:
        count_rounds += 1
        split_the_command = [item for item in command.split(" ")]
        divide_by = int(split_the_command[1])
        if divide_by == 0:
            print("ZeroDivisionError caught")
        else:
            divided_nums = [int(num) / divide_by for num in nums]
            print(divided_nums)

    elif "slice" in command:
        count_rounds += 1
        split_the_command = [item for item in command.split(" ")]
        start_index = int(split_the_command[1])
        end_index = int(split_the_command[2])
        if start_index < 0 or start_index > len(nums) - 1:
            print("IndexError caught")
        elif end_index > len(nums) - 1 or end_index < 0:
            print("IndexError caught")
        else:
            print(nums[start_index:end_index + 1])

    elif command == "sort":
        count_rounds += 1
        print(sorted(nums))

    elif command == "reverse":
        count_rounds += 1
        reversed_list = [int(item) for item in reversed(nums)]
        print(reversed_list)

print(f"I beat It for {count_rounds} rounds!")
