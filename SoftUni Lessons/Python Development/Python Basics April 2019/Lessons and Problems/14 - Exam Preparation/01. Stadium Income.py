count_sectors = int(input())
capacity = int(input())
price_one_ticket = float(input())

total_income = price_one_ticket * capacity
sector_income = total_income / count_sectors
charity = (total_income - (sector_income * 0.75)) / 8

print(f"Total income - {total_income:.2f} BGN")
print(f"Money for charity - {charity:.2f} BGN")
