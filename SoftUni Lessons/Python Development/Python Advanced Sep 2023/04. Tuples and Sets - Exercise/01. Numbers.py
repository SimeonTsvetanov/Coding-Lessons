sets = {
    'First': set([int(n) for n in input().split(' ')]),
    'Second': set([int(n) for n in input().split(' ')])
}

for each_time in range(int(input())):
    data = input().split(' ')
    command = data.pop(0)
    curr = data.pop(0)

    if command == 'Add':
        nums = set(list(map(int, data)))
        sets[curr] = sets[curr].union(set(list(map(int, data))))

    elif command == "Remove":
        [sets[curr].remove(num) for num in set(list(map(int, data))) if num in sets[curr]]

    elif command == "Check":
        print(sets['First'].issubset(sets['Second']) or sets['Second'].issubset(sets['First']))

[print(', '.join([str(x) for x in sorted(list(sets[x]))])) for x in ['First', 'Second']]
