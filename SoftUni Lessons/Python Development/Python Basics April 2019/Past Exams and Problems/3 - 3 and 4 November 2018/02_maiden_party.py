price_maiden_party = float(input())
count_love_letters = int(input())
count_waxed_roses = int(input())
count_key_rings = int(input())
count_cartoon = int(input())
count_lucky_surprise = int(input())

count_total = count_love_letters + count_waxed_roses + count_key_rings + count_cartoon + count_lucky_surprise

price_love_letters = count_love_letters * 0.6
price_waxed_roses = count_waxed_roses * 7.2
price_key_rings = count_key_rings * 3.6
price_cartoon = count_cartoon * 18.20
price_lucky_surprise = count_lucky_surprise * 22

price_total = price_love_letters + price_waxed_roses + price_key_rings + price_cartoon + price_lucky_surprise

if count_total >= 25:
    price_total -= price_total * 0.35

price_total -= price_total * 0.1

if price_total >= price_maiden_party:
    print(f"Yes! {(price_total - price_maiden_party):.2f} lv left.")
else:
    print(f"Not enough money! {(price_maiden_party - price_total):.2f} lv needed.")
