owned_eggs = int(input())
sold_eggs = owned_eggs

total_sold_eggs = 0
command = None
count = 0

while command != "Close" or not(sold_eggs < 0):
    command = input()
    if command == "Close":
        break
    count = int(input())
    if command == "Fill":
        sold_eggs += count
    if command == "Buy":
        sold_eggs -= count
        total_sold_eggs += count
    if sold_eggs < 0:
        break

if command == "Close":
    print("Store is closed!")
    print(f"{total_sold_eggs} eggs sold.")

if sold_eggs < 0:
    print("Not enough eggs in store!")
    print(f"You can buy only {sold_eggs + count}.")
