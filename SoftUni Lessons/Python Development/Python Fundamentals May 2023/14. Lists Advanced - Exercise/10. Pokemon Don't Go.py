distances = [int(n) for n in input().split(' ')]
sum_value_removed_elements = 0

while distances:
    index = int(input())
    if index < 0:
        element = distances[0]
        sum_value_removed_elements += element
        del distances[0]
        distances.insert(0, distances[-1])
    elif index >= len(distances):
        element = distances[-1]
        sum_value_removed_elements += element
        del distances[-1]
        distances.append(distances[0])
    else:
        element = distances[index]
        del distances[index]
        sum_value_removed_elements += element
    distances = [n + element if n <= element else n - element for n in distances]


print(sum_value_removed_elements)
