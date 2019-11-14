start_symbol = ord(input())
end_symbol = ord(input())
skip_symbol = ord(input())

total_combinations = 0

for x1 in range(start_symbol, end_symbol + 1):
    for x2 in range(start_symbol, end_symbol + 1):
        for x3 in range(start_symbol, end_symbol + 1):
            if x1 != skip_symbol and x2 != skip_symbol and x3 != skip_symbol:
                total_combinations += 1
                print(f"{chr(x1)}{chr(x2)}{chr(x3)}", end=" ")
print(total_combinations)



