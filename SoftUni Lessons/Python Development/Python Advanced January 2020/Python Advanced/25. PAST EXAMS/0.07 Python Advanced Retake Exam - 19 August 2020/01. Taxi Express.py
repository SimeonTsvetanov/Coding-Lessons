# 60../100 in Judje NO IDEA why. This is rediculas.

customers = [int(c) for c in input().split(", ")]
taxis = [int(t) for t in input().split(", ")]

total_time = 0

while customers and taxis:
    customer = customers.pop(-1)
    taxi = taxis.pop(0)
    if taxi >= customer:
        total_time += customer
    elif taxi < customer:
        customers.append(customer)

if len(customers) == 0:
    print(f"All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print(f"Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(c) for c in customers])}")
