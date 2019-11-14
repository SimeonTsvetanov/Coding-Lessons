count_pc = int(input())
average_rating = 0
total_sales = 0

for i in range(count_pc):
    command = int(input())
    rating = command % 10
    average_rating += rating
    possible_sales = int(str(command)[:2])
    if rating == 2:
        total_sales += 0
    elif rating == 3:
        total_sales += possible_sales / 2
    elif rating == 4:
        total_sales += possible_sales * 0.7
    elif rating == 5:
        total_sales += possible_sales * 0.85
    elif rating == 6:
        total_sales += possible_sales

print(f"{total_sales:.2f}")
print(f"{(average_rating / count_pc):.2f}")


