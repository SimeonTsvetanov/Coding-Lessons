"""
# This is from work at home:
class Book:
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages


book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)
"""


# And this is the solution from work in class:
class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


# When we use __dict__ we can see all the attributes stored in the object as dictionary:
print(Book("xxx", "yyy", 3).__dict__)
# We can also add *args and *kwargs in the class attributes
