# Write a program that receives two numbers (factor and count)
factor = int(input())
count = int(input())

# . It should create a list with a length of the given
# count that contains only integer numbers,
# which are multiples of the given factor.
# The numbers should be only positive,
# and they should be arranged in ascending order,
# starting from the value of the factor.

nums = []
current = factor

for num in range(count):
    nums.append(current)
    current = current + factor


print(nums)
