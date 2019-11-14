"""
Technology Fundamentals Retake Mid Exam - 16 April 2019
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1610#2

SUPyF2 P.-Mid-Exam/16 April 2019 - 03. Easter Shopping

Problem:
You have decided to go on an Easter shopping spree to take advantage of the promotions.
Create a program that helps you keep track of the shops that you want to visit.
You will receive the list of shops you have planned on checking out on a single line,
separated by a single space in the following format:
"{shop1} {shop2} {shop3}… {shopn}"
Then you will receive a number – n - a count of commands you need to execute over your list.
There are four possible commands:
•	"Include {shop}":
o	Add the shop at the end of your list.
•	"Visit {first/last} {numberOfShops}"
o	Remove either the "first" or the "last" number of shops from your list, depending on the input.
If you have less shops on your list than the given number, skip this command.
•	"Prefer {shopIndex1} {shopIndex2}":
o	If both of the shop indexes exist in your list, take the shops that are on them and change their places.
•	"Place {shop} {shopIndex}"
o	Insert the shop after the given index, only if the resulted index exists.
In the end print the manipulated list in the following format:
"Shops left:
{shop1} {shop2}… {shopn}"
Input / Constraints
•	On the 1st line, you will receive the starting list with the names of the shops separated by a single space.
•	On the 2nd line, you will receive the number of commands - n – an integer in range [1…100]
•	On the next n lines you will be receiving commands in the format described above.
Output
•	Print the list after the manipulations in the format described above.
Examples:
Input:
Bershka CandyStore ThriftShop Armani Groceries ToyStore PeakStore
5
Include HM
Visit first 2
Visit last 1
Prefer 3 1
Place Library 2

Output:
Shops left:
ThriftShop ToyStore Groceries Library Armani PeakStore

Comments:
First we receive the "Include" and the name of the store and we add the store to our list.
The list should look like this: Bershka CandyStore ThriftShop Armani Groceries ToyStore PeakStore HM
After, we receive the "Visit" command and "first", which means we have to visit the first 2 stores,
so we remove them from our list and the collection should look like this:
ThriftShop Armani Groceries ToyStore PeakStore HM. After that, we receive the "Visit" command again,
but this time we need to visit the "last" 1 store, so we remove it and the collection should look like this:
ThriftShop Armani Groceries ToyStore PeakStore. After that we receive the "Prefer" command,
which means we need to find the shop on the first given index – 3 and change it with the one that is on index – 1,
and the collection should look like this: ThriftShop ToyStore Groceries Armani PeakStore.
At last, we receive the "Place" command and we need to insert the shop at the next index after 2.
And our final list looks like this:
ThriftShop ToyStore Groceries Library Armani PeakStore

Input:
Boutique Flowers CandyStore ThriftShop Versace Groceries ToyStore PeakStore
6
Visit first 9
Visit last 4
Prefer 3 8
Prefer 0 1
Place Store 7
Place ShoeAquarium 2

Output:
Shops left:
Flowers Boutique CandyStore ShoeAquarium ThriftShop
"""
shops = input().split()

for i in range(int(input())):
    command = input().split()

    if command[0] == "Include":
        new_shop = command[1]
        shops.append(new_shop)

    elif command[0] == "Visit":
        first_or_last, number_of_shops = command[1], int(command[2])
        if number_of_shops <= len(shops):
            if first_or_last == "first":
                shops = shops[number_of_shops:]
            elif first_or_last == "last":
                shops = shops[:-number_of_shops]

    elif command[0] == "Prefer":
        shop_index_one, shop_index_two = int(command[1]), int(command[2])
        if 0 <= shop_index_one < len(shops) and 0 <= shop_index_two < len(shops):
            shops[shop_index_one], shops[shop_index_two] = shops[shop_index_two], shops[shop_index_one]

    elif command[0] == "Place":
        shop, shop_index = command[1], int(command[2]) + 1
        if 0 <= shop_index < len(shops):
            shops.insert(shop_index, shop)

print(f"Shops left:\n{' '.join(shops)}")
