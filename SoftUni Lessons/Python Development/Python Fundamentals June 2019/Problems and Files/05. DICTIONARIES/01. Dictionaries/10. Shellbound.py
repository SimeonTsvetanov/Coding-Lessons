"""
Dictionaries and Functional Programming
Проверка: https://judge.softuni.bg/Contests/Practice/Index/945#9

SUPyF Dictionaries - 10. Shellbound

Problem:
Vladi is a crab. Crabs are scared of almost anything, which is why they usually hide in their shells. Vladi 
is a rich crab though. He has acquired many outer shells, in different regions, in which he can hide – 
each with a different size. 
However, it is really annoying to look after all your shells when they are so spread out. That is why Vladi decided 
to merge all shells in each region, so that he has one big shell for every region. He needs your help to do that.
You will be given several input lines containing a string and an integer, separated by a space. The string will 
represent the region’s name, and the integer – the shell in the given region, size. 
You must store all shells in their corresponding regions.
If the region already exists, add the new shell to it. Make sure you have NO duplicate shells (shells with same size). 
Vladi doesn’t like shells to have the same size.
When you receive the command “Aggregate”, you must stop reading input lines, and you must print every region, all of 
the shells in that region, and the size of the giant shell after you’ve merged them in the following format:
{regionName} -> {shell 1, shell 2…, shell n…} ({giantShell})
The giant shell size is calculated when you subtract the average of the shells from the sum of the shells.
Or in other words: (sum of shells) – ((sum of shells) / (count of shells)).
Constraints
- All numeric data will be represented with integer variables in range [0…1.000.000.000].
Examples:
Input:
Sofia 50
Sofia 20
Sofia 30
Varna 10
Varna 20
Aggregate
OutPut:
Sofia -> 50, 20, 30 (67)
Varna -> 10, 20 (15)
"""
import math
regions = {}
while True:
    command = input()
    if command == "Aggregate":
        break
    a = [item for item in command.split(" ")]
    if a[0] not in regions:
        regions[a[0]] = [a[1]]
    else:
        if a[1] not in regions[a[0]]:
            regions[a[0]] += [a[1]]
        else:
            continue

for region, value in regions.items():
    print(f"{region} -> ", end="")
    print(", ".join(value), end=" ")
    sum_of_value = 0
    count_value = len(value)
    for i in value:
        sum_of_value += int(i)
    grand_crab = math.ceil(sum_of_value - (sum_of_value / count_value))
    print(f"({grand_crab})")

    
def another_solution():
    import math

    regions = {}

    while True:
        command = input().split(" ")
        if command[0] == "Aggregate":
            break

        region = command[0]
        shell = int(command[1])

        if region not in regions.keys():
            regions[region] = [shell]
        else:
            if shell not in regions[region]:
                regions[region].append(shell)

    for region, shells in regions.items():
        giant_shell = math.ceil((sum(shells)) - (sum(shells) / len(shells)))
        print(f"{region} -> {', '.join(str(sh) for sh in shells)} ({giant_shell})")


# another_solution()
