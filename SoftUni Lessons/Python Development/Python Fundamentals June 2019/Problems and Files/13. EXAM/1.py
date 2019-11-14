n = int(input())

m = float(input())
count_of_reviews = 0

for i in range(n):
    coded_message = input()

    if coded_message.isdigit():
        counter = 0
        dummy_number = ""
        all_digits = []
        secret_word_from_digits = ""
        for digit in coded_message:
            counter += 1
            dummy_number += digit
            if counter == 2:
                secret_word_from_digits += chr(int(dummy_number))
                counter = 0
                all_digits += [dummy_number]
                dummy_number = ""
        print(f"Reviewing item - {secret_word_from_digits}")
        count_of_reviews += 1
    if coded_message.isalpha():
        reversed_word = str(str(letter) for letter in reversed(coded_message))
        print(f"Reviewing location - ", end="")
        print(''.join(list(reversed(coded_message))))
        count_of_reviews += 1

print(f"{count_of_reviews} reviews have been made this month. Salary: {(count_of_reviews * m):.2f}")
