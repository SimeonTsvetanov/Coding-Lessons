def bakery():
    bakery_stock = {}
    stock_input = input().split(" ")
    for index in range(0, len(stock_input), 2):
        bakery_stock[stock_input[index]] = int(stock_input[index + 1])
    print(bakery_stock)


def stock():
    def sort_the_bakery():
        bakery_stocking = {}
        stock_input = input().split(" ")
        for index in range(0, len(stock_input), 2):
            bakery_stocking[stock_input[index]] = int(stock_input[index + 1])
        return bakery_stocking

    bakery_stock = sort_the_bakery()
    for product in input().split(" "):
        if product in bakery_stock.keys():
            print(f"We have {bakery_stock[product]} of {product} left")
        else:
            print(f"Sorry, we don't have {product}")


def statistics():
    products = {}

    while True:
        command = input().split(": ")
        if command[0] == "statistics":
            break

        product = command[0]
        quantity = int(command[1])

        if product not in products.keys():
            products[product] = quantity
        else:
            products[product] += quantity

    print("Products in stock:")
    for product, quantity in products.items():
        print(f"- {product}: {quantity}")
    print(f"Total Products: {len(products)}")
    print(f"Total Quantity: {sum(products.values())}")


def students():
    courses = {}
    searched_course = ""

    while True:
        command = input()
        if not (":" in command):
            searched_course = command.replace('_', ' ')
            break

        name, ids, course = command.split(":")
        if course not in courses.keys():
            courses[course] = {}
        courses[course][ids] = name

    for ids, name in courses[searched_course].items():
        print(f"{name} - {ids}")


def ascii_values():
    dictionary = {letter: ord(letter) for letter in input().split(", ")}
    print(dictionary)


def odd_occurrences():
    words = [word.lower() for word in input().split(" ")]
    words_dict = {word: words.count(word) for word in words}
    for word, count in words_dict.items():
        if count % 2 != 0:
            print(word, end=' ')


def word_synonyms():
    synonyms = {}

    for each_time in range(int(input())):
        word, synonym = input(), input()
        if word not in synonyms:
            synonyms[word] = [synonym]
        else:
            synonyms[word].append(synonym)

    for word, synonym_words in synonyms.items():
        print(f"{word} - {', '.join(synonym_words)}")


if __name__ == '__main__':
    # bakery()
    # stock()
    # statistics()
    # students()
    # ascii_values()
    # odd_occurrences()
    word_synonyms()
