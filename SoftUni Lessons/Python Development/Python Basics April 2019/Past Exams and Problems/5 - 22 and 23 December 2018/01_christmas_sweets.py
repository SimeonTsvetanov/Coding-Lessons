price_baklava_kg = float(input())
price_muffin_kg = float(input())
kg_shtolen = float(input())
kg_candies = float(input())
kg_biscuits = int(input())

price_shtolen = price_baklava_kg + (price_baklava_kg * 0.6)
total_shtolen = price_shtolen * kg_shtolen

price_candies = price_muffin_kg + (price_muffin_kg * 0.8)
total_candies = price_candies * kg_candies

total_biscuits = 7.5 * kg_biscuits

total = total_shtolen + total_candies + total_biscuits

print(f"{total:.2f}")

