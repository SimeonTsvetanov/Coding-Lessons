def stock_availability(boxes: list, del_or_sel: str, *args):
    stock = [box for box in boxes]
    if del_or_sel == "delivery":
        if len(args) > 0:
            [stock.append(arg) for arg in args]
    elif del_or_sel == "sell":
        if len(args) > 0:
            if str(args[0]).isdigit():
                for index in range(int(args[0])):
                    stock.pop(0)
            else:
                for product in args:
                    while product in stock:
                        stock.remove(product)
        else:
            stock.pop(0)
    return stock


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))


