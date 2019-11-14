count_chicken_menu = int(input())
count_fish_menu = int(input())
count_vegetarian_menu = int(input())

total_menu = (count_chicken_menu * 10.35) + (count_fish_menu * 12.40) + (count_vegetarian_menu * 8.15)
dessert = total_menu * 0.2
delivery = 2.5
total = total_menu + dessert + delivery

print(f"Total: {total:.2f}")