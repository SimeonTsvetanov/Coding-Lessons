num = int(input())

odd_sum = 0
max_odd = -999999999999999
min_odd = 999999999999999

even_sum = 0
max_even = -999999999999999
min_even = 999999999999999

for i in range(1, num + 1):
    in_num = float(input())
    if i % 2 != 0:
        odd_sum += in_num
        if in_num > max_odd:
            max_odd = in_num
        if in_num < min_odd:
            min_odd = in_num
    elif i % 2 == 0:
        even_sum += in_num
        if in_num > max_even:
            max_even = in_num
        if in_num < min_even:
            min_even = in_num


print(f"OddSum={odd_sum:.2f},")
if min_odd == 999999999999999:
    print("OddMin=No,")
else:
    print(f"OddMin={min_odd:.2f},")
if max_odd == -999999999999999:
    print("OddMax=No,")
else:
    print(f"OddMax={max_odd:.2f},")

print(f"EvenSum={even_sum:.2f},")
if min_even == 999999999999999:
    print("EvenMin=No,")
else:
    print(f"EvenMin={min_even:.2f},")
if max_even == -999999999999999:
    print("EvenMax=No")
else:
    print(f"EvenMax={max_even:.2f}")


