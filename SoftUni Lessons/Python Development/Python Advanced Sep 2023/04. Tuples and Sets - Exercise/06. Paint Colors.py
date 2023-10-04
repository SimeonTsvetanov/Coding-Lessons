from collections import deque

raw_string = deque(input().split())
main_colours_model = ["red", "yellow", "blue"]
secondary_colours_model = ["orange", "purple", "green"]
colours_main = []
colours_secondary = []
all_colours = []

while raw_string:
    if len(raw_string) == 1:
        left_str = raw_string.popleft()
        right_str = ''
    else:
        left_str = raw_string.popleft()
        right_str = raw_string.pop()

    if left_str + right_str in main_colours_model:
        colours_main.append(left_str + right_str)
        all_colours.append(left_str + right_str)
    elif right_str + left_str in main_colours_model:
        colours_main.append(right_str + left_str)
        all_colours.append(right_str + left_str)

    elif left_str + right_str in secondary_colours_model:
        colours_secondary.append(left_str + right_str)
        all_colours.append(left_str + right_str)
    elif right_str + left_str in secondary_colours_model:
        colours_secondary.append(right_str + left_str)
        all_colours.append(right_str + left_str)

    else:
        left_str = left_str[0:len(left_str) - 1]
        right_str = right_str[0:len(right_str) - 1]
        if left_str:
            raw_string.insert(len(raw_string) // 2, left_str)
        if right_str:
            raw_string.insert(len(raw_string) // 2, right_str)

secondary_formation_dict = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue'],
}
result = []

for x in all_colours:
    if x in colours_main:
        result.append(x)
    else:
        is_valid = True
        for k, v in secondary_formation_dict.items():
            if k == x:  # here
                # print(secondary_formation_dict[k][::])
                contains_secondary = all([el in colours_main for el in v])
                if contains_secondary:
                    result.append(k)

print(result)