count_pencils = int(input())
count_markers = int(input())
liter_desk_soap = float(input())
percent_discount = int(input())

price_pencils = count_pencils * 5.8
price_markers = count_markers * 7.20
price_desk_soap = liter_desk_soap * 1.2

price = price_pencils + price_markers + price_desk_soap

price = price - ((price * percent_discount) / 100)

print(f"{price:.3f}")

