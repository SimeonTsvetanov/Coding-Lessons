numbers_list = list(map(int, input().split()))
manipulated_numbers_list = []


while True:
    data = input()
    if data == "exhausted":
        break
    data_list = data.split()
    command = data_list[0]

    if command == "set":
        if len(set(numbers_list)) == len(numbers_list):
            print("It is a set")
        manipulated_numbers_list = list(set(numbers_list))
    elif command == "filter":
        pass
    elif command == "multiply":
        pass
    elif command == "divide":
        pass
    elif command == "slice":
        pass
    elif command == "sort":
        pass
    elif command == "reverse":
        pass
