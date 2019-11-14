"""
Basics OOP Principles
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/1556#1

SUPyF Basics OOP Principles - 02. Book Shop

Problem:
You are working in a library. You are sick of writing descriptions for books by hand,
so you wish to use the computer to speed up the process. The task is simple - your program should have two classes –
one for the ordinary books – Book, and another for the special ones – GoldenEditionBook.
So let’s get started! We need two classes:
- Book - represents a book that holds title, author and price.
A book should offer information about itself in the format shown in the output below.
- GoldenEditionBook - represents a special book that holds the same properties as any Book,
    but its price is always 30% higher.

Constraints:
- If the author’s second name is starting with a digit –  the exception’s message is: "Author not valid!"
- If the title’s length is less than 3 symbols –  the exception’s message is: "Title not valid!"
- If the price is zero or it is negative – the exception’s message is: "Price not valid!"
- Price must be formatted to two symbols after the decimal separator

Examples:
    Input:
        Ivo 4ndonov
        Under Cover
        9999999999999999999
    Output:
        Author not valid!

    Input:
        Petur Ivanov
        Life of Pesho
        20
    Output:
        Type: Book
        Title: Life of Pesho
        Author: Petur Ivanov
        Price: 20.00

        Type: GoldenEditionBook
        Title: Life of Pesho
        Author: Petur Ivanov
        Price: 26.00
"""

"""
HELP:
Step 1 - Create a Book Class
Create a new empty class and name it Book. 

Step 2 - Define the Properties of a Book
Define the Title, Author and Price properties of a Book. 

Step 3 - Define a Constructor
Define a constructor that accepts author, title and price arguments.

Step 4 - Perform Validations
Create a field for each property (Price, Title and Author) and perform validations for each one. 
The getter should return the corresponding field and the setter should validate the input data before setting it. 
Do this for every property.

Step 5 - Override __str__()
We have already mentioned that all of the classes in C# inherit the System.Object class and therefore have 
all its public members. 
Let's override (change)  the ToString() method’s behavior again according to our Book class’s data.

And voila! If everything is correct, we can now create Book objects and display information about them.

Step 6 – Create a GoldenEditionBook
Create a GoldenEditionBook class that inherits Book and has the same constructor definition. However, 
do not copy the code from the Book class - reuse the Book class constructor.
There is no need to rewrite the Price, 
Title and Author properties since GoldenEditionBook inherits Book and by default has them.

Step 7 - Override the Price Property
Golden edition books should return a 30% higher price than the original price. 
In order for the getter to return a different value, we need to override the Price property. 
Back to the GoldenEditionBook class, let's override the Price property and change the getter body
"""

class Book:
    def __init__(self, author, title, price):
        self.author = author
        self.title = title
        self.price = price
        self.type = "Book"

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def price(self):
        return self._price

    @title.setter
    def title(self, title):
        if len(str(title)) < 3:
            raise Exception("Title not valid!")
        else:
            self._title = title

    @author.setter
    def author(self, author):
        data = author.split()
        if len(data) > 1:
            first_letter = data[1][0]
            if first_letter.isdigit():
                raise Exception("Author not valid!")
            else:
                self._author = author
        else:
            self._author = author

    @price.setter
    def price(self, price):
        if price <= 0:
            raise Exception("Price not valid!")
        else:
            self._price = price

    def __str__(self):
        return f"Type: {self.type}" + "\n" + f"Title: {self.title}" + "\n" + f"Author: {self.author}" + "\n" +\
               f"Price: {self.price:.2f}"


class GoldenEditionBook(Book):
    def __init__(self, author, title, price):
        Book.__init__(self, author, title, price)
        self.price = self.price + (self.price * 0.3)
        self.type = "GoldenEditionBook"


name_author = input()
name_book = input()
book_price = float(input())

try:
    b1 = Book(name_author, name_book, book_price)
    print(b1)
    print()
    b2 = GoldenEditionBook(name_author, name_book, book_price)
    print(b2)
except Exception as e:
    print(e)
