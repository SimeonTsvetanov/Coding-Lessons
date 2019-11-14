def wtf():
    print("Would you like to try this program?")
    print("You have to answer with yes or no and press enter")
    print("Just advice if you say no I will send you in a LOOP>>>>")
    command = input()
    if command == "yes":
        start_menu()
    else:
        no()


def start_menu():
    print("In this program You can try all 7 of the tasks from LISTS(file 3):")
    print("To continue Just type down the task number (1, 2,3 .... 7) and press Enter.")
    print()
    print()
    command = input()
    if command == "1":
        task1()
    elif command == "2":
        task2()
    elif command == "3":
        task3()
    elif command == "4":
        task4()
    elif command == "5":
        task5()
    elif command == "6":
        task6()
    elif command == "7":
        task7()


def task1():
    print("You have selected Task 01. Array Contains Element")
    print("Write down a list of integers on the first line of the console like:(1 2 3 4 5 6 7) and then press Enter")
    print("After that write down a number You wish to check if its in the list you added first and press Enter again")
    print("And I will give you and answer, by confirming with yes or no.")
    nums = [int(item) for item in input().split(" ")]
    num = int(input())
    print("Result:")
    if num in nums:
        print("yes")
    else:
        print("no")
    print()
    print()
    start_menu()


def task2():
    print("You have selected Task 02. Smallest Element in Array")
    print("Here you will give me a whole list of integers and I will tell you which is the smallest one.")
    print("Write down a list of integers like (1 2 3 4 5 6 7 8 9) And press ENTER")
    print()
    print()
    nums = [int(item) for item in input().split(" ")]
    print("Result:")
    print(min(nums))
    print()
    print()
    start_menu()


def task3():
    print("You have selected Task 03. Reverse Array In-place")
    print("You can give me a whole list of integers and I will reverse it for you.")
    print("So just type down your list. Like (1 2 3 4 5 6 7 8) and press Enter")
    nums = [int(item) for item in input().split(" ")]

    nums.reverse()
    print("Result:")
    for num in nums:
        print(num, end=" ")
    print()
    print()
    start_menu()


def task4():
    print("You have selected Task 04. Sort Array Using Bubble Sort")
    print("You can give me a whole list of integers and I will sort it for you. Using the Bubble Sort Method")
    print("Just type down your list like (1 2 3 4 5 6 7 8) and press Enter")

    def short_bubble_sort(a_list):
        exchanges = True
        pass_num = len(a_list) - 1
        while pass_num > 0 and exchanges:
            exchanges = False
            for i in range(pass_num):
                if a_list[i] > a_list[i + 1]:
                    exchanges = True
                    temp = a_list[i]
                    a_list[i] = a_list[i + 1]
                    a_list[i + 1] = temp
            pass_num = pass_num - 1

    nums = [int(item) for item in input().split(" ")]
    short_bubble_sort(nums)
    print("Result:")
    for num in nums:
        print(num, end=" ")
    print()
    print()
    start_menu()


def task5():
    print("You have selected Task 05. Sort Array Using Insertion Sort")
    print("You can give me a whole list of integers and I will sort it for you. Using the Insertion Sort Method")
    print("Just type down your list like (1 2 3 4 5 6 7 8) and press Enter")

    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    nums = [int(item) for item in input().split(" ")]
    insertion_sort(nums)
    print("Result:")
    for num in nums:
        print(num, end=" ")


def task6():
    print("You have selected Task 6. Insertion Sort Using List")
    print("You can give me a whole list of integers and I will sort it for you. Using the Insertion Sort Method")
    print("Just type down your list like (1 2 3 4 5 6 7 8) and press Enter")

    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    nums = [int(item) for item in input().split(" ")]
    insertion_sort(nums)
    print(f"Result:")
    for num in nums:
        print(num, end=" ")
    print()
    print()
    start_menu()


def no():
    while True:
        print("You HAD to say YES.")


def task7():
    print("You have selected Task 07. Largest N Elements")
    print("Here you will give me a whole list of integers. And a specific X number. I will sort the list for you")
    print("in reverse order and i will show you the X number of items you have asked for.")
    print("So first type down your list like (1 2 3 4 5 6 7 8) and press Enter")
    nums = [int(item) for item in input().split(" ")]
    print(f"Now type down your X number:")
    count = int(input())

    nums.sort(reverse=True)

    start = 0
    sorted_nums = []

    while count != 0:
        sorted_nums += [nums[start]]
        start += 1
        count -= 1
    print("Result:")
    for num in sorted_nums:
        print(num, end=" ")
    print()
    print()
    start_menu()


wtf()


