easter_bread = int(input())
eggs_cartoon = int(input())
kilo_biscuits = int(input())

price_easter_bread = easter_bread * 3.2
price_eggs = eggs_cartoon * 4.35
price_biscuits = kilo_biscuits * 5.4
price_eggs_paint = 0.15 * (eggs_cartoon * 12)

total = price_easter_bread + price_eggs + price_biscuits + price_eggs_paint

print(f"{total:.2f}")


