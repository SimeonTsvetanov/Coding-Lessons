# Quickly define a function with a return value on one line:
"""
square = lambda num: num ** 2

checker = False
while not checker:
    try:
        print(square(int(input("Pls, enter a number to get it's square:   "))))
        checker = True
    except ValueError:
        print("not a valid input try again")

#  This same function can be done with
#  def square(num):
#    return num ** 2
#  print(square(5))
"""
# Lambda functions can be anonymous:
# We can do the one from above with out giving it a name.

#  print((lambda num: num ** 2)(5))  # връща 25

# Functional Programming: filter()

"""
# filter() let us filter any iterable by passing it trough a function
nums = [1, 2, 3, 4, 5]


def is_even(num):
    return num % 2 == 0


even_nums = list(filter(lambda num: num % 2 == 0, nums))
print(*even_nums)
"""

"""
# map let us transform each element in a list:
nums = [1, 2, 3]


def increment_by_two(num):
    return num + 2


incremented_nums = list(map(increment_by_two, nums))
print(*incremented_nums)

# Or we can do all that on one line with Lambda:
print(*(list(map(increment_by_two, nums))))
"""

"""
Using zip() to combine items at identical positions into tuples:
cords_x = [1, 2, 3]
cords_y = [22, 14, 5]

zipped_cords = zip(cords_x, cords_y)
# [(1, 22), (2, 14), (3, 5)]
Using zip() with more than 2 iterables:
cords_z = [46, 22, 45]
zipped_cords = zip(cords_x, cords_y, cords_z)
# [(1, 22, 46), (2, 14, 22), (3, 5, 45)]
"""

# WE can use map to convert items in different types:
#  nums = ["1", "2", "3", "4"]
#  parsed_nums = map(int, nums)  # here the first argument (int) is to parse the strings from the list above into ints.
#  print(*parsed_nums)

# And we can ise map for the str.join(): as this method only works on strings.
# nums = [1, 2, 3]
# print(", ".join(nums))  # This will give us a Type ERROR
# print(", ".join(map(str, nums)))  # This will convert all the ints from nums and print them as a string.

"""
Moved to functools library in Python 3
We have to use:  from functools import reduce


from functools import reduce
nums = [1, 2, 3, 4, 5]
nums_sum = reduce(lambda a, b: a + b, nums)  # 15
print(nums_sum)
nums_product = reduce(lambda a, b: a * b, nums)  # 120
print(nums_product)
"""

# We can be using sorted() to sort a collection’s items in ascending order.
# OR, Using reversed() to reverse a collection.

"""
We can sort a dictionary by the count of it's values:

student_grades = {
    'Ivan': [3, 4],
    'Petar': [5, 2, 5],
    'Maria': [6, 6, 5, 6],
    'Gosho': [5, 6]
}
sorted_grades = \
  sorted(student_grades.items(), key=lambda kvp: len(kvp[1]))  # - this is key value pair with two elements.

for name, grades in sorted_grades:
    print('{}: {}'.format(name, grades))
"""

# We can do the same but instead of soring the elements only by the count. We can add extra option if the count is
# Equal to sort them by key:
"""
sorted_grades = \
    sorted(student_grades.items(),
           key=lambda kvp: (len(kvp[1]), kvp[0]))
"""

""" 
Сега малко съмари на материята до тук:
- речниците съдържат двойки от: ключ -> стойност.
    .keys съдържа сет от уникални ключове.
    .values съдържа колекция от стойности.
- Можем да решаваме по-сложни задачи с малко по- малко код използвайки функционалното програмиране:
    - filter/map/reduce
    - zip/sorted/reverse
"""

