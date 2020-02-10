def work_at_home_task_three():
    text = input()
    try:
        times = int(input())
        print(text*times)
    except ValueError:
        print("Variable times must be an integer")


def work_in_class_task_three():
    def solve(text, times):
        try:
            if not isinstance(times, int):
                raise TypeError("Variable times must be an integer")
            print(text * times)
        except TypeError as err:
            print(err)

    solve("Pesho", 3)
    solve("Pesho", 3.4)
    solve("Pesho", "Gosho")


if __name__ == '__main__':
    # work_at_home_task_three()
    work_in_class_task_three()
