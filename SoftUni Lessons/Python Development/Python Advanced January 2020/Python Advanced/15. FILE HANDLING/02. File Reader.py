def work_at_home_file_reader():
    nums = open('numbers.txt', 'r')
    total = 0
    for num in nums:
        total += int(num)
    print(total)


def work_in_class_file_reader():
    file = open('files\\numbers.txt', 'r')

    the_sum = 0
    for line in file:
        the_sum += int(line)
    print(the_sum)


if __name__ == '__main__':
    # work_at_home_file_reader()
    work_in_class_file_reader()

