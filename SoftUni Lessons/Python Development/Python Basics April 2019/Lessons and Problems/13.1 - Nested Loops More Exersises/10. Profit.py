count_coins_1_lv = int(input())
count_coins_2_lv = int(input())
count_bills_5_lv = int(input())
amount = int(input())

for coin_1 in range(count_coins_1_lv + 1):
    for coin_2 in range(count_coins_2_lv + 1):
        for bill_5 in range(count_bills_5_lv + 1):
            if (coin_1 * 1) + (coin_2 * 2) + (bill_5 * 5) == amount:
                print(f"{coin_1} * 1 lv. + {coin_2} * 2 lv. + {bill_5} * 5 lv. = {amount} lv.")
