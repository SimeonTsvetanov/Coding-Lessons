def work_at_home_task_sort():
    print(abs(sum([int(num) for num in input().split(" ") if int(num) < 0])))


def work_in_class_task_sort():
    numbers = map(int, input().split())
    negative = filter(lambda x: x < 0, numbers)
    print(abs(sum(negative)))


if __name__ == '__main__':
    # work_at_home_task_sort()
    work_in_class_task_sort()
