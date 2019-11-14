num = int(input())

magic_num = num

first_digit = num // 100
second_digit = (num % 100) // 10
third_digit = num % 10

number_of_rows = first_digit + second_digit
number_of_colons = first_digit + third_digit

for number in range(number_of_rows):
    for number2 in range(number_of_colons):
        if magic_num % 5 == 0:
            magic_num -= first_digit
        elif magic_num % 3 == 0:
            magic_num -= second_digit
        else:
            magic_num += third_digit
        print(f"{magic_num}", end=" ")
    print()




