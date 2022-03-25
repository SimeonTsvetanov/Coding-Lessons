orders = [int(p) for p in input().split(", ") if (0 < int(p) <= 10)]
capacities = list(map(int, input().split(", ")))

finished = 0

while orders and capacities:
    order = orders[0]
    capacity = capacities[-1]
    if capacity >= order:
        finished += order
        orders.pop(0)
        capacities.pop(-1)
    else:
        remaining = order - capacity
        done = order - remaining
        capacities.pop(-1)
        orders[0] = remaining
        finished += done

if len(orders) == 0:
    print(f"All orders are successfully completed!")
    print(f"Total pizzas made: {finished}")
    print(f"Employees: {', '.join([str(e) for e in capacities])}")
else:
    print(f"Not all orders are completed.")
    print(f"Orders left: {', '.join([str(o) for o in orders])}")
