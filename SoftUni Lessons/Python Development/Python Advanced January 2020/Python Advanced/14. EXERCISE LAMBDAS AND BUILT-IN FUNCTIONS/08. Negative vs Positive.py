def work_at_home_task_negative_or_positive():
    nums = [int(num) for num in input().split(" ")]
    negative_nums_sum = sum([num for num in nums if num < 0])
    positive_nums_sum = sum([num for num in nums if num >= 0])
    print(negative_nums_sum), print(positive_nums_sum)
    if abs(negative_nums_sum) > positive_nums_sum:
        print(f"The negatives are stronger than the positives")
    else:
        print(f"The positives are stronger than the negatives")


def work_in_class_task_negative_or_positive():
    numbers = list(map(int, input().split()))
    negative_sum = sum(filter(lambda x: x < 0, numbers))
    positive_sum = sum(filter(lambda x: x > 0, numbers))
    print(negative_sum)
    print(positive_sum)

    if abs(negative_sum) > positive_sum:
        print(f"The negatives are stronger than the positives")
    else:
        print(f"The positives are stronger than the negatives")


if __name__ == '__main__':
    # work_at_home_task_negative_or_positive()
    work_in_class_task_negative_or_positive()
