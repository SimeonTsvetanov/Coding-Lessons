longest_intersection = set()

for i in range(int(input())):
    intersection_one, intersection_two = input().split("-")
    start_int_one, end_int_one = [int(x) for x in intersection_one.split(",")]
    start_int_two, end_int_two = [int(x) for x in intersection_two.split(",")]

    current_set_int_one = set()
    current_set_int_two = set()

    for num in range(start_int_one, end_int_one + 1):
        current_set_int_one.add(num)
    for num in range(start_int_two, end_int_two + 1):
        current_set_int_two.add(num)

    current_intersection = current_set_int_one & current_set_int_two
    if len(current_intersection) >= len(longest_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is {sorted(list(longest_intersection))} with length {len(longest_intersection)}")
