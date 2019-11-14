import math
import sys
easter_bread = int(input())

total_sugar = 0
total_flour = 0

max_flour = -sys.maxsize - 1
max_sugar = -sys.maxsize - 1

for i in range(easter_bread):
    sugar = int(input())
    total_sugar += sugar
    if sugar > max_sugar:
        max_sugar = sugar
    flour = int(input())
    total_flour += flour
    if flour > max_flour:
        max_flour = flour


print(f"Sugar: {math.ceil(total_sugar / 950)}")
print(f"Flour: {math.ceil(total_flour / 750)}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
