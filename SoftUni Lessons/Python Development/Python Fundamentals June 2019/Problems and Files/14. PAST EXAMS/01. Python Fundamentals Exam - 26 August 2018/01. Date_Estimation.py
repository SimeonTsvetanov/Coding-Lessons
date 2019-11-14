from datetime import date
date_input = [int(item) for item in input().split("-")]
input_year = date_input[0]
input_month = date_input[1]
input_day = date_input[2]

today_list = [2018, 8, 26]
today_year = 2018
today_month = 8
today_day = 26

d0 = date(today_year, today_month, today_day)
d1 = date(input_year, input_month, input_day)

if d0 == d1:
    print("Today date")
elif today_year == input_year:
    if today_month == input_month:
        if today_day > input_day:
            print("Passed")
    elif today_month > input_month:
        print("Passed")
    else:
        delta = d1 - d0
        print(f"{delta.days + 1} days left")
else:
    delta = d1 - d0
    print(f"{delta.days + 1} days left")
