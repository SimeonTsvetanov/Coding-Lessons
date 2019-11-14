"""
Lists Basics - More Exercises
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1726#2

SUPyF2 Lists More Exercise - 03. Josephus Permutation

Problem:
This problem takes its name by arguably the most important event in the life of the ancient historian Josephus:
according to his tale, he and his 40 soldiers were trapped in a cave by the Romans during a siege.
Refusing to surrender to the enemy, they instead opted for mass suicide, with a twist:
they formed a circle and proceeded to kill one man every three, until one last man was left
(and that it was supposed to kill himself to end the act). Well, Josephus and another man were the last two and,
as we now know every detail of the story,
you may have correctly guessed that they didn't exactly follow through the original idea.
You are now to create a program that prints a Josephus permutation, receiving two lines of code (the list itself
(string with elements separated by a single space) and a number k)
as if they were in a circle and counted out every k places until none remained.

Example:
Input:
1 2 3 4 5 6 7
3
Output:
[3,6,2,7,5,1,4]
"""

"""
    global dead
    skip -= 1
    position_ti_kill = skip
    while True:
        dead += [still_alive_list.pop(position_ti_kill)]
        if len(still_alive_list) == 0:
            break
        position_ti_kill = (position_ti_kill + skip) % len(still_alive_list)
    return print("[" + ",".join(dead) + "]")
"""
alive = [element for element in input().split()]
k = int(input())
dead = []


def josephus(still_alive_list, skip):
    for times in range(skip):
        first_element = still_alive_list[0]
        if first_element == 0:
            break
        else:
            still_alive_list.remove(first_element)
            still_alive_list.append(first_element)
        dead.append(still_alive_list[0])
        still_alive_list.remove(still_alive_list[0])
    return print("[" + ",".join(dead) + "]")


josephus(alive, k)

