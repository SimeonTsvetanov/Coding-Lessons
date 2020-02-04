def work_at_home_task_odd_or_even():
    command = input()
    nums = [int(num) for num in input().split(" ")]
    if command == "Odd":
        print(sum([num for num in nums if num % 2 != 0]) * len(nums))
    elif command == "Even":
        print(sum([num for num in nums if num % 2 == 0]) * len(nums))


def work_in_class_task_odd_or_even():
    def number_filter(command_, *args):
        remainder = 0 if command_ == "Even" else 1
        return filter(lambda x: x % 2 == remainder, args)

    command = input()
    numbers = list(map(int, input().split()))

    filtered_sum = sum(number_filter(command, *numbers)) * len(numbers)
    print(filtered_sum)


if __name__ == '__main__':
    # work_at_home_task_odd_or_even()
    work_in_class_task_odd_or_even()
