time_for_break = int(input())
price_one_peripheral_part = float(input())
price_one_program = float(input())
price_white_frappe = float(input())

remaining_time = time_for_break - 15

price_peripheral = 3 * price_one_peripheral_part
price_programs = 2 * price_one_program

total_spend_money = price_peripheral + price_programs + price_white_frappe

print(f"{total_spend_money:.2f}")
print(remaining_time)
