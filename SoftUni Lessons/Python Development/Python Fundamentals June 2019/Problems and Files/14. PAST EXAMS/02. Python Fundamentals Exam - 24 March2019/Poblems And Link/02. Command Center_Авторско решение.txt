def are_indexes_in_range(index1, index2, my_list):
    if len(my_list) > index1 >= 0 and len(my_list) > index2 >= 0:
        return True
    return False


def swap(index1, index2, my_list):
    index1 = int(index1)
    index2 = int(index2)
    if are_indexes_in_range(index1, index2, my_list):
        current_el = my_list[index1]
        my_list[index1] = my_list[index2]
        my_list[index2] = current_el
    return my_list


def get_divisible(_, number, my_list):
    return list(filter(lambda x: x % int(number) == 0.0, my_list))


def enumerate_list(my_list):
    return list(enumerate(my_list))


command_center = [swap, enumerate_list, max, min, get_divisible]

input_list = list(map(int, input().split()))

data = input()
performed_commands = 0

while not data == 'end':
    splitted_data = data.split()
    command = splitted_data[0]
    for function in command_center:
        if function.__name__ == command:
            if len(splitted_data) == 1:
                result = function(input_list)
            else:
                result = function(splitted_data[1], splitted_data[2], input_list)
            print(result)
            performed_commands += 1
            break

    data = input()

print(performed_commands)