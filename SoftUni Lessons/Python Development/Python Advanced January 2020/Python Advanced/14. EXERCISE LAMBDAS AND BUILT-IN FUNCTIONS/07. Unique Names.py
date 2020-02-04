def work_at_home_task_unique_names():
    sum_len_valid_names = sum([len(name) for name in input().split() if name[0].isupper() and name[1:].islower()])
    print(sum_len_valid_names)


def work_in_class_task_unique_names():
    names = input().split()
    filtered = filter(lambda x: x.istitle(), names)
    sum_length = sum(map(lambda x: len(x), filtered))
    print(sum_length)


if __name__ == '__main__':
    # work_at_home_task_unique_names()
    work_in_class_task_unique_names()
