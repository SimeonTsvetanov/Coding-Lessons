def work_at_home_task_sort_numbers():
    initial_list = [word_or_num for word_or_num in input().split(" ")]
    bigger_nums_only = sorted([int(num) for num in initial_list if num.isdigit() and int(num) > len(initial_list)])
    print(' '.join([str(num) for num in bigger_nums_only]))


def work_in_class_task_sort_numbers():
    line = input().split()
    numbers = filter(lambda x: x.isdigit(), line)
    numbers = filter(lambda x: x > len(line), map(int, numbers))
    sorted_numbers = sorted(numbers)
    print(*sorted_numbers)


if __name__ == '__main__':
    # work_at_home_task_sort_numbers()
    work_in_class_task_sort_numbers()
