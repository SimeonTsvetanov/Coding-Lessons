price_flour_kg = float(input())
kilo_flour = float(input())
kilo_sugar = float(input())
eggs_cartoon = int(input())
packets_yeast = int(input())

price_flour = price_flour_kg * kilo_flour
price_sugar_kg = price_flour_kg - (price_flour_kg * 0.25)
price_sugar = (price_flour_kg - (price_flour_kg * 0.25)) * kilo_sugar
price_eggs = (price_flour_kg + (price_flour_kg * 0.1)) * eggs_cartoon
price_flour_kg_yeast = (price_sugar_kg - (price_sugar_kg * 0.8)) * packets_yeast

total = price_flour + price_sugar + price_eggs + price_flour_kg_yeast
print(f"{total:.2f}")
