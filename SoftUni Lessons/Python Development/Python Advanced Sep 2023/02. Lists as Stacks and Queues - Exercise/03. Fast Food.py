"""
You have a fast-food restaurant, and the food you are offering is previously prepared.
Write a program that checks if you have enough food to serve lunch to all your customers. You also want to know who
the client with the biggest order for that day is
"""

# First, you will be given the quantity of food you have for the day (an integer number).
food = int(input())

# Next, you will be given a sequence of integers (separated by a single space)
# each representing the quantity of food in each order. Keep the orders in a queue.
queue = [int(n) for n in input().split(' ')]


# Find the biggest order and print it:
biggest_order = max(queue)
print(biggest_order)

# Next, you will begin servicing your clients from the first one that came.
# Before each order, check if you have enough food left to complete it:

while queue:
    client = queue[0]
    # If you have, remove the order from the queue and reduce the quantity of food in the restaurant.
    if food - client >= 0:
        food -= client
        queue.pop(0)
    # Otherwise, stop serving.
    else:
        break

# If you succeeded in servicing all your clients, print: "Orders complete"
if not queue:
    print("Orders complete")
# Otherwise, print: "Orders left: {order1} {order2} .... {orderN}"
else:
    print(f"Orders left: {' '.join([str(n) for n in queue])}")
