from project.user import User


class Library:
    def __init__(self):
        self.user_records = []  # [user1, user2, user3...]
        self.books_available = {}  # {author: [book1, book2, book2...]}
        self.rented_books = {}  # ({usernames: {book names: days to return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if author in self.books_available and book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)
            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}
            self.rented_books[user.username][book_name] = days_to_return
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        already_rented = [[[n, d] for n, d in data.items() if n == book_name] for u, data in self.rented_books.items()]
        if already_rented:
            book = already_rented[0][0]
            print(book)
            return f'The book "{book[0]}" is already rented and will be available in {book[1]} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"

        user.books.remove(book_name)

        if author not in self.books_available:
            self.books_available[author] = []
        self.books_available[author].append(book_name)

        for user_name, books in self.rented_books.items():
            if user_name == user.username:
                if book_name in books:
                    del books[book_name]
