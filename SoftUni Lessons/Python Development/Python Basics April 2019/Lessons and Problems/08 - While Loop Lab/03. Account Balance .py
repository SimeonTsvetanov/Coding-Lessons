input_times = int(input())

total = 0

while input_times != 0:
    income_input = float(input())
    if income_input < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {income_input:.2f}")
    total += income_input
    input_times -= 1

print(f"Total: {total:.2f}")

