def work_at_home_task_two():
    class ValueCannotBeNegative(Exception):
        """Number is below zero"""
        pass

    for i in range(5):
        number = int(input())
        if number < 0:
            raise ValueCannotBeNegative


def work_in_class_task_two():
    class ValueCannotBeNegative(Exception):
        """
        Raised when at least one of the values is not a int
        """
        pass

    class ValueCannotBeNegativeError(Exception):
        """
        Raised when value is negative
        """
        pass

    nums = [1, 2, 3, 4, 5]

    for _ in range(5):
        num = input()

    for num in nums:
        if num < 0:
            raise ValueCannotBeNegativeError


if __name__ == '__main__':
    # work_at_home_task_two()
    work_in_class_task_two()
