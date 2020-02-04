def work_at_home_task_multiplication():
    multiplicand = int(input())
    nums = [int(num) * multiplicand for num in input().split(" ")]
    print(' '.join([str(num) for num in nums]))


def work_in_class_task_multiplication():
    n = int(input())
    numbers = map(int, input().split())
    multiplied = map(lambda x: x * n, numbers)
    print(*multiplied)


if __name__ == '__main__':
    # work_at_home_task_multiplication()
    work_in_class_task_multiplication()
