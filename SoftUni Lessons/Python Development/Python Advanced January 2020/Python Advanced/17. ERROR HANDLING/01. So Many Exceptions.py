def work_at_home_task_one():
    nums = '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11'

    numbers_list = [int(num) for num in nums.split(", ")]
    result = 1
    for i in range(len(numbers_list)):
        number = numbers_list[i]
        if number <= 5:
            result *= number
        elif 5 < number <= 10:
            result /= number
    print(result)


def work_in_class_task_one():
    def multiply(*args):
        result = 1
        args_len = len(args)

        for i in range(args_len):
            number = int(args[i])
            if number <= 5:
                result *= number
            elif 5 < number <= 10:
                result /= number
        return result

    print(multiply(1, 4, 5))
    print(multiply(4, 5, 6, 1, 3))
    print(multiply(2, 0, 1000, 5000))
    print(multiply(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


if __name__ == '__main__':
    # work_at_home_task_one()
    work_in_class_task_one()
