alpinist = int(input())
carabiners = int(input())
ropes = int(input())
pickels = int(input())

carabiners_price = 36 * carabiners
ropes_price = 3.60 * ropes
pickels_price = 19.80 * pickels

total_price = (carabiners_price + ropes_price + pickels_price) * alpinist

total_price += total_price * 0.2

print(f"{total_price:.2f}")