num = int(input())
counter = 0

for x1 in range(66, 77):
    for x2 in range(102, 96, -1):
        for x3 in range(65, 68):
            for x4 in range(1, 11):
                for x5 in range(10, 0, -1):
                    if x1 % 2 == 0:
                        counter += 1
                        if counter == num:
                            print(f"Ticket combination: {chr(x1)}{chr(x2)}{chr(x3)}{x4}{x5}")
                            print(f"Prize: {x1 + x2 + x3 + x4 + x5} lv.")
