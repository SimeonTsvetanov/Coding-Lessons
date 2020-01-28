def words_lengths():
    print(', '.join([f"{word} -> {length}" for word, length in {word: len(word) for word in input().split(", ")}.items()]))


def number_classification():
    numbers = [int(x) for x in input().split(", ")]
    print(f"Positive: {', '.join([str(x) for x in numbers if x >= 0])}")
    print(f"Negative: {', '.join([str(x) for x in numbers if x < 0])}")
    print(f"Even: {', '.join([str(x) for x in numbers if x % 2 == 0])}")
    print(f"Odd: {', '.join([str(x) for x in numbers if x % 2 != 0])}")


def diagonals():
    n = int(input())
    matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]
    primary_diagonal = [matrix[i][i] for i in range(n)]
    secondary_diagonal = [matrix[i][n - i - 1] for i in range(n)]
    print(f"First diagonal: {', '.join([str(num) for num in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
    print(f"Second diagonal: {', '.join([str(num) for num in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")


def capitals():
    countries = input().split(", ")
    capital_cities = input().split(", ")
    [print(f"{country} -> {capital}") for country, capital in zip(countries, capital_cities)]


def heroes_inventory():
    names = input().split(", ")
    heroes = {hero: {} for hero in names}
    command = input()
    while command != "End":
        name, item, cost = command.split("-")
        if name in heroes:
            if item not in heroes[name]:
                heroes[name][item] = int(cost)
        command = input()
    [print(f"{hero} -> Items: {len(items)}, Cost: {sum([amount for item, amount in items.items()])}") for hero, items in heroes.items()]


def bunkers():
    categories = input().split(", ")
    bunker = {category: {} for category in categories}
    n = int(input())
    for _ in range(n):
        tokens = input().split(" - ")
        category = tokens[0]
        item = tokens[1]
        item_info = tokens[2].split(";")
        quantity = int(item_info[0].split(":")[1])
        quality = int(item_info[1].split(":")[1])
        if category in bunker:
            bunker[category][item] = {"quantity": quantity, "quality": quality}
    count_items = sum([bunker[x][y]["quantity"] for x in bunker for y in bunker[x]])
    sums_quality = sum([bunker[x][y]["quality"] for x in bunker for y in bunker[x]])
    average_quality = sums_quality / len(categories)
    print(f"Count of items: {count_items}")
    print(f"Average quality: {average_quality:.2f}")
    [print(f"{category} -> {', '.join(bunker[category].keys())}") for category in bunker]


if __name__ == '__main__':
    # words_lengths()  # 1st
    # number_classification()  # 2nd
    # diagonals()  # 3th
    # capitals()  # 4th
    # heroes_inventory()  # 5th
    bunkers()  # 6th
