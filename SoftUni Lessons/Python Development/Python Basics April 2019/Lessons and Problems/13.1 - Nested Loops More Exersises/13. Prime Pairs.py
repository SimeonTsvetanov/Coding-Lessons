start_first_couple = int(input())
start_second_couple = int(input())
difference_between_start_end_first_couple = int(input())
difference_between_start_end_second_couple = int(input())

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

for couple_1 in range(start_first_couple, start_first_couple + difference_between_start_end_first_couple + 1):
    for couple_2 in range(start_second_couple, start_second_couple + difference_between_start_end_second_couple + 1):
        if couple_1 in prime_numbers and couple_2 in prime_numbers:
            print(f"{couple_1}{couple_2}")
