population = [int(x) for x in input().split(', ')]
minimum_wealth = int(input())

average = sum(population) / len(population)

if average >= minimum_wealth:
    while True:
        if all([x >= minimum_wealth for x in population]):
            print(population)
            break

        biggest = max(population)
        index_biggest = population.index(biggest)
        smallest = min(population)
        index_smallest = population.index(smallest)

        needed = minimum_wealth - smallest

        can_give = 0
        while True:
            if (biggest <= minimum_wealth) or (can_give == needed):
                break
            can_give += 1
            biggest -= 1

        population[index_biggest] = biggest
        population[index_smallest] += can_give
else:
    print('No equal distribution possible')
