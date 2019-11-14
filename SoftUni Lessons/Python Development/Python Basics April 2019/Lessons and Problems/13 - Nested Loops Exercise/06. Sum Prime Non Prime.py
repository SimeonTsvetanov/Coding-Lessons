sum_prime = 0
sum_not_prime = 0

while True:
    command = input()
    if command == "stop":
        break
    num = int(command)
    if num < 0:
        print("Number is negative.")
        continue
    if num == 0 or num == 1:
        sum_not_prime += num
        continue
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                is_prime = False
                break
        else:
            is_prime = True
    else:
        is_prime = False
    if is_prime:
        sum_prime += num
    else:
        sum_not_prime += num

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_not_prime}")



