my_list = [int(item) for item in input().split()]

while True:
    command = input().split()
    if command[0] == "END":
        break
    elif command[0] == "multiply" and command[1] == "list":
        multiply_times = int(command[2])
        my_list = my_list * multiply_times

    elif command[0] == "multiply" and command[1].isdigit() and command[2].isdigit():
        element_in_list = int(command[1])
        multiply_by = int(command[2])
        my_list = [(int(x) * multiply_by) if x == element_in_list else int(x) for x in my_list]
    if command[0] == "contains":
        print(my_list.__contains__(int(command[1])))
    if command[0] == "add":
        if command[1].isdigit():
            my_list += [int(command[1])]
        else:
            new_list = [int(item) for item in command[1].split(",")]
            my_list += new_list

my_list = [int(item) for item in my_list]
my_list.sort()

my_list = [str(item) for item in my_list]

print(" ".join(my_list))



