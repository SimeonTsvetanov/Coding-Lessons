num1 = int(input())
num2 = int(input())

for i in range(num1, num2 + 1):

    left_sum = 0
    middle = 0
    right_sum = 0

    n5 = i % 10
    n4 = int(i / 10) % 10
    n3 = int(i / 100) % 10
    n2 = int(i / 1000) % 10
    n1 = int(i / 10000) % 10

    left_sum += n1 + n2
    middle += n3
    right_sum += n4 + n5

    if left_sum == right_sum:
        print(i, end=" ")
    else:
        if left_sum > right_sum:
            right_sum += middle
            if left_sum == right_sum:
                print(i, end=" ")
        elif right_sum > left_sum:
            left_sum += middle
            if right_sum == left_sum:
                print(i, end=" ")
