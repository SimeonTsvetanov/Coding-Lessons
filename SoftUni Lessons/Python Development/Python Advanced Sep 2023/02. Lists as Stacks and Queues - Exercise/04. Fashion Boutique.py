# You own a fashion boutique and receive a delivery of a huge box of clothes, represented as a sequence of integers.
clothes = [int(x) for x in input().split()]

# In the following line, you will be given an integer representing the capacity for one rack in your store:
rack = int(input())

"""
You must arrange the clothes in the store and use the racks to hang up every piece of clothing. You start from the last
piece of clothing on the top of the pile to the first one at the bottom. Use a stack for this purpose. Each piece of
clothing has its value (an integer). You must sum their values while you take them out of the box:
"""

rack_count = 0
total = 0

while clothes:
    current = clothes[-1]
    # If the sum becomes equal to the capacity of the current rack, you must take a new one for the next clothes
    # (if there are any left in the box).
    if rack >= total + current:
        total += clothes.pop()
    else:
        # If the sum becomes greater than the capacity, do not hang the piece of clothing on the current rack. Take a
        # new rack and then hang it up.
        total = 0
        rack_count += 1

# In the end, print how many racks you have used to hang up the clothes:
rack_count += 1 if total > 0 else 'pass'
print(rack_count)
