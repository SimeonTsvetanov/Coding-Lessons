bitcoin = int(input())
chinese_yuan = float(input())
commission = float(input())

total_bitcoin_in_lev = 1168 * bitcoin
chinese_yuan_in_usd = 0.15 * chinese_yuan
chinese_yuan_in_lv = chinese_yuan_in_usd * 1.76
total = (total_bitcoin_in_lev + chinese_yuan_in_lv) / 1.95

commission = commission / 100
total -= total * commission

print(f"{total:.2f}")
