"""
Technology Fundamentals Final Exam - 14 April 2019 Group I
link: https://judge.softuni.bg/Contests/Practice/Index/1516#1
Name: 01. 02. On the Way to Annapurna
"""
shops = []
while True:
    data = input().split("->")
    if data[0] == "END":
        break
    if data[0] == "Add":
        shop_in_list = False
        for shop in shops:
            if shop[0] == data[1]:
                shop += [item for item in data[2].split(",")]
                shop_in_list = True
                break
        if not shop_in_list:
            shops += [[data[1]] + [item for item in data[2].split(",")]]
    elif data[0] == "Remove":
        for shop in shops:
            if shop[0] == data[1]:
                shops.remove(shop)

shops = sorted(sorted(shops, key=lambda x: x[0], reverse=True), key=lambda x: len(x), reverse=True)

print(f"Stores list:")
for shop in shops:
    print(shop[0])
    for item in shop[1:]:
        print(f"<<{item}>>")

