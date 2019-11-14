start_number = int(input())
end_number = int(input()) + 1

for num_1 in range(start_number, end_number):
    for num_2 in range(start_number, end_number):
        for num_3 in range(start_number, end_number):
            for num_4 in range(start_number, end_number):
                if (num_1 % 2 == 0 and num_4 % 2 != 0) or (num_1 % 2 != 0 and num_4 % 2 == 0):
                    if num_1 > num_4:
                        sum_2_and_3 = num_2 + num_3
                        if sum_2_and_3 % 2 == 0:
                            print(f"{num_1}{num_2}{num_3}{num_4}", end=" ")
