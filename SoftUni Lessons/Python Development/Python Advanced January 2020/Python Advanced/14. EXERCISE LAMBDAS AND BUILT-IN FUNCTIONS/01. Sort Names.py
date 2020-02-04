def work_at_home_task_sort_names():
    print(" ".join(sorted([name for name in input().split(" ")], reverse=True)))


def work_in_class_task_sort_names():
    names = input().split()
    sorted_names = sorted(names, reverse=True)
    print(*sorted_names)


if __name__ == '__main__':
    # work_at_home_task_sort_names()
    work_in_class_task_sort_names()
