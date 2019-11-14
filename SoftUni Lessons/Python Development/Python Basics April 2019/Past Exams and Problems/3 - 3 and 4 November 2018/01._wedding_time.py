price_whiskey = float(input())
volume_water_liters = float(input())
volume_wine_liters = float(input())
volume_champagne_liters = float(input())
volume_whiskey_liters = float(input())


price_champagne = price_whiskey * 0.5
price_wine = price_champagne * 0.4
price_water = price_champagne * 0.1

whiskey = price_whiskey * volume_whiskey_liters
water = price_water * volume_water_liters
wine = price_wine * volume_wine_liters
champagne = price_champagne * volume_champagne_liters

total = whiskey + water + wine + champagne

print(f"{total:.2f}")

