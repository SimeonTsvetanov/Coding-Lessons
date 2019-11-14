"""
Lists Advanced - More Exercises
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1732#2

SUPyF2 Lists Advanced-More-Ex. - 03. Take/Skip Rope

Problem:
A core idea of several left-wing ideologies is that the wealthiest should support the poorest,
no matter what and that is exactly what you are called to do for this problem.
On the first line you will be given the population (numbers separated by comma and space ", ").
On the second line you will be given the minimum wealth.
You have to distribute the wealth, so that there is no part of the population that has less than the minimum wealth.
To do that, you should always take wealth from the wealthiest part of the population.
There will be cases, where the distribution will not be possible. In that case, print "No equal distribution possible"
Example
Input	                Output
2, 3, 5, 15, 75         [5, 5, 5, 15, 70]
5

2, 3, 5, 15, 75         [20, 20, 20, 20, 20]
20

2, 3, 5, 45, 45         No equal distribution possible
30
"""
population = [int(number) for number in input().split(", ")]
minimum_wealth = int(input())

if sum(population) < (minimum_wealth * len(population)):
    print("No equal distribution possible")
else:
    while True:
        if population[0] >= minimum_wealth:
            break
        population[-1] -= 1
        population[0] += 1
        population.sort()
    print(population)
