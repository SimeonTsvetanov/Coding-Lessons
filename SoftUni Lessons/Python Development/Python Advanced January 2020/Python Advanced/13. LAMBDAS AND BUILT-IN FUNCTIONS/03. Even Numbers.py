def solution_from_work_in_class():
    numbers = map(int, input().split(" "))
    result = filter(lambda x: x % 2 == 0, numbers)
    print(list(result))


if __name__ == '__main__':
    solution_from_work_in_class()
