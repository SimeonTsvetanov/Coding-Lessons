# You will be given numbers separated by a space
numbers = [float(n) for n in input().split(' ')]

# Write a program that prints the number of occurrences of each
# number in the format "{number} - {count} times". The number must be formatted to the first decimal point.

{print(f"{number:.1f} - {count} times") for number, count in {num: numbers.count(num) for num in numbers}.items()}
