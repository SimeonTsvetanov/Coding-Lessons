def simple_solution():
    """
    The simpler way of solving it:
    """
    start = int(input())
    end = int(input()) + 1

    def get_divisible(num):
        for divider in range(2, 10):
            if num % divider == 0:
                return True
        return False

    nums_list = [num for num in range(start, end) if get_divisible(num)]
    print(nums_list)


def complected_solution():
    """
    And the more complicated way:
    """
    print([num for num in range(int(input()), (int(input()) + 1)) if any([num % x == 0 for x in range(2, 10)])])


if __name__ == '__main__':
    # simple_solution()
    complected_solution()
