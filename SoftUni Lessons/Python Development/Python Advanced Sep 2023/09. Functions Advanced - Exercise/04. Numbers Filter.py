def even_odd_filter(**kwargs):
    dictionary = {}
    for command, nums in kwargs.items():
        if command == 'even':
            if 'even' not in dictionary:
                dictionary['even'] = []
            [dictionary['even'].append(x) for x in nums if x % 2 == 0]
        elif command == 'odd':
            if 'odd' not in dictionary:
                dictionary['odd'] = []
            [dictionary['odd'].append(x) for x in nums if x % 2 != 0]

    sorted_dict = dict(sorted(dictionary.items(), key=lambda x: -len(x[1])))
    return sorted_dict


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
