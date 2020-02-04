def work_at_home_task_unique_numbers():
    nums = [round(float(num)) for num in input().split()]
    print(min(nums)), print(max(nums))
    nums = sorted(list(set([num * 3 for num in nums])))
    print(' '.join([str(num) for num in nums]))


def work_in_class_task_unique_numbers():
    numbers = list(map(lambda x: round(float(x)), input().split()))
    print(min(numbers))
    print(max(numbers))
    multiplied = map(lambda x: x * 3, numbers)
    unique = sorted(set(multiplied))
    print(*unique)


if __name__ == '__main__':
    # work_at_home_task_unique_numbers()
    work_in_class_task_unique_numbers()
