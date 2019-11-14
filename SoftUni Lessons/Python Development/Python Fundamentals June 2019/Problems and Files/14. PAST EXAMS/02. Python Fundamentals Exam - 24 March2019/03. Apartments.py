"""
Basics OOP Principles
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/1590#2

SUPyF Exam 24.03.2019 - 03. Apartments

Problem:
Input / Constraints
We have the task to create database for a businessman, who buys apartments in different neighborhoods here in Sofia.
At the first stage he does a research for available apartments.
He will give you a neighborhood name and a list of block numbers in format:
{neighborhood} -> {block_num,block_num,block_num}
When you receive the command ‘collectApartments’ you should stop adding research results and start assigning them with
the real data. Note that the businessman can give you a neighborhood or a block number which haven’t been researched.
In this case just do nothing, but if he gives you a researched neighborhood and a researched block number in this
neighborhood assign the values for it. The data will come in the following format:

{ neighborhood}&{block_number} -> {count_of_available_apartments}|{price_for_one_apartment}

It’s  possible to receive existing neighborhood and block_number and already assigned count_of_available_apartments
with given price. In this case REPLACE  the old info with the new one.
Output
When you recieve a command which says 'report', you should print all apartments data ordered by name of the neighborhood
ascending after that by block_number ascending in the following format:
Neighborhood: {neighborhood}
* Block number: {block_number} -> { count_of_available_apartments } apartments for sale. Price for one: {price_for_one_apartment }
•	If  there is no available apartments in this block in this neighborhood just print 0 for the available apartments count.
•	If there is no price, just print for price_for_one_apartment ‘None’.

Examples:
    Input:
        Lozenec -> 11,2
        Durvenica -> 4,3
        Mladost1 -> 5,2
        Mladost2 -> 7,8
        collectApartments
        Lozenec&11 -> 2|100000
        Lozenec&2 -> 1|100000
        Durvenica&3 -> 5|80000
        Durvenica&5 -> 15|80000
        Mladost2&13 -> 6|80000
        Mladost1&13 -> 7|79000
        report
    Output:
        Neighborhood: Durvenica
        * Block number: 3 -> 5 apartments for sale. Price for one: 80000
        * Block number: 4 -> 0 apartments for sale. Price for one: None
        Neighborhood: Lozenec
        * Block number: 2 -> 1 apartments for sale. Price for one: 100000
        * Block number: 11 -> 2 apartments for sale. Price for one: 100000
        Neighborhood: Mladost1
        * Block number: 2 -> 0 apartments for sale. Price for one: None
        * Block number: 5 -> 0 apartments for sale. Price for one: None
        Neighborhood: Mladost2
        * Block number: 7 -> 0 apartments for sale. Price for one: None
        * Block number: 8 -> 0 apartments for sale. Price for one: None
"""
# Here we have 2 ways to solve the problem first option is with Classes:


class Block:
    def __init__(self, block_number: int, count_apartments=0, price_one=None):
        self.block_number = block_number
        self.count_apartments = count_apartments
        self.price_one = price_one


class Neighborhood:
    def __init__(self, name, blocks: []):
        self.name = name
        self.blocks = blocks


all_neighborhoods = []

while True:
    data = input()
    if data == "collectApartments":
        break
    c_neighborhood, all_blocks = data.split(" -> ")
    c_blocks = [Block(block_number=int(block)) for block in all_blocks.split(",")]
    neigh = Neighborhood(name=c_neighborhood, blocks=c_blocks)

    if_neighborhood_exist = False
    for neighborhood in all_neighborhoods:
        if neighborhood.name == neigh.name:
            if_neighborhood_exist = True

            for checked_block in neigh.blocks:
                if_block_exist = False
                for block in neighborhood.blocks:
                    if checked_block.block_number == block.block_number:
                        if_block_exist = True
                if not if_block_exist:
                    neighborhood.blocks += [Block(block_number=int(checked_block.block_number))]

    if not if_neighborhood_exist:
        all_neighborhoods += [neigh]


all_neighborhoods.sort(key=lambda x: x.name, reverse=False)
for neighborhood in all_neighborhoods:
    neighborhood.blocks.sort(key=lambda x: x.block_number)

while True:
    data = input()
    if data == "report":
        break
    neigh_and_block, av_and_pr = data.split(" -> ")
    r_neighborhood, r_bock = neigh_and_block.split("&")
    r_av_ap, r_price = av_and_pr.split("|")
    r_bock = int(r_bock)

    for neigh in all_neighborhoods:
        if r_neighborhood == neigh.name:
            for bl in neigh.blocks:
                if bl.block_number == r_bock:
                    bl.count_apartments = r_av_ap
                    bl.price_one = r_price
                    break

for n in all_neighborhoods:
    print(f"Neighborhood: {n.name}")
    for b in n.blocks:
        print(f"* Block number: {b.block_number} -> {b.count_apartments} apartments for sale. Price for one: {b.price_one}")


# The second way to solve the problem is to use dictionary (which i hate from the depth of my heart):
"""
apartments = {}

data_list = input().split(' -> ')

while not data_list[0] == 'collectApartments':
    neighborhood = data_list[0]
    blocks_nums = list(map(int, data_list[1].split(',')))

    if neighborhood not in apartments.keys():
        apartments[neighborhood] = {}
    for num in blocks_nums:
        apartments[neighborhood][num] = {'available_apartments_count': 0, 'price': None}

    data_list = input().split(' -> ')

data_list = input().split(' -> ')

while not data_list[0].strip() == 'report':
    neighborhood, block_num = data_list[0].split('&')
    count_available, price = list(map(int, data_list[1].split('|')))
    block_num = int(block_num)

    if neighborhood in apartments.keys() and block_num in apartments[neighborhood].keys():
        apartments[neighborhood][block_num]['available_apartments_count'] = count_available
        apartments[neighborhood][block_num]['price'] = price

    data_list = input().split(' -> ')

for neighborhood, _ in sorted(apartments.items(), key=lambda kvp: kvp[0]):
    print(f"Neighborhood: {neighborhood}")
    for block_num, info_dict in sorted(apartments[neighborhood].items(), key=lambda kvp: kvp[0]):
        print(
            f"* Block number: {block_num} -> {info_dict['available_apartments_count']} apartments for sale. Price for one: {info_dict['price']}")
"""
