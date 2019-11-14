searched_book = input()
number_of_books = int(input())

counter = 0
is_found = False

current_book = input()

while counter < number_of_books:
    if current_book == searched_book:
        is_found = True
        break
    counter += 1
    if counter == number_of_books:
        break
    current_book = input()
if is_found:
    print(f"You checked {counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")

