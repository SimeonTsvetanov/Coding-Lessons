def work_at_home_task_whole_number():
    nums = [round(float(num)) for num in input().split(" ")]
    print(sum(nums) * len(nums))


def work_in_class_task_whole_number():
    numbers = list(map(lambda x: round(float(x)), input().split()))
    numbers_sum = sum(numbers) * len(numbers)
    print(numbers_sum)


if __name__ == '__main__':
    # work_at_home_task_whole_number()
    work_in_class_task_whole_number()
