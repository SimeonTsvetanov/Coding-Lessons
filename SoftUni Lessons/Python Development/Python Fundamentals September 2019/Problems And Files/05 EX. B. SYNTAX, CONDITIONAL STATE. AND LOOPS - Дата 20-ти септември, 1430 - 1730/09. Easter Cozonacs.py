"""
Basic Syntax, Conditional Statements and Loops - Exercise
Check your code: https://judge.softuni.bg/Contests/Compete/Index/1719#8
Video: https://www.youtube.com/watch?time_continue=4&v=7sHE4HEUqi8

SUPyF2 Basic Exercise - 09. Easter Cozonacs (not included in final score)

Problem:
Since it’s Easter you have decided to make some cozonacs and exchange them for eggs.
Create a program that calculates how much cozonacs you can make with the budget you have. First,
you will receive your budget. Then, you will receive the price for 1 kg flour. Here is the recipe for one cozonac:
Eggs	1 pack
Flour	1 kg
Milk	0.250 l
The price for 1 pack of eggs is 75% of the price for 1 kg flour.
The price for 1l milk is 25% more than price for 1 kg flour. Notice,
that you need 0.250l milk for one cozonac and the calculated price is for 1l.
Start cooking the cozonacs and keep making them until you have enough budget. Keep in mind that:
•	For every cozonac that you make, you will receive 3 colored eggs.
•	For every 3rd cozonac that you make, you will lose some of your colored eggs after you have received the usual 3
colored eggs for your cozonac. The count of eggs you will lose is calculated when you subtract 2 from your current
count of cozonacs – ({currentCozonacsCount} – 2)
In the end, print the cozonacs you made, the eggs you have gathered and the money you have left,
formatted to the 2nd decimal place, in the following format:
"You made {countOfCozonacs} cozonacs! Now you have {coloredEggs} eggs and {moneyLeft}BGN left."
Input / Constraints
•	On the 1st line you will receive the budget – a real number in the range [0.0…100000.0]
•	On the 2nd line you will receive the price for 1 kg floor – a real number in the range [0.0…100000.0]
•	The input will always be in the right format.
•	You will always have a remaining budget.
•	There will not be a case in which the eggs become a negative count.
Output
•	In the end print the count of cozonacs you have made, the colored eggs you have gathered and the money formatted to
the 2nd decimal place in the format described above.

Examples:
Input:
20.50
1.25
Output:
You made 7 cozonacs! Now you have 16 eggs and 2.45BGN left.

Input:
15.75
1.4

Output:
You made 5 cozonacs! Now you have 14 eggs and 1.31BGN left.
"""

budget = float(input())
price_1kg_flour = float(input())
price_1_pack_eggs = price_1kg_flour * 0.75
price_1l_milk = price_1kg_flour * 1.25
price_250ml_milk = price_1l_milk / 4
total_price_1_cozonac = price_1kg_flour + price_1_pack_eggs + price_250ml_milk
count_eggs = 0
count_cozonacs = 0
while True:
    if budget - total_price_1_cozonac < 0:
        break
    else:
        count_cozonacs += 1
        budget -= total_price_1_cozonac
        count_eggs += 3

        if count_cozonacs % 3 == 0:
            count_lost_eggs = count_cozonacs - 2
            count_eggs -= count_lost_eggs

print(f"You made {count_cozonacs} cozonacs! Now you have {count_eggs} eggs and {budget:.2f}BGN left.")
