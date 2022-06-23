function bookShelf (data) {
    // MasK
    // ... I just don't have the patience to solve more inception based associative arrays!!!
    //     So from now on I'll do them with Classes and Objects instead for more fun.

    class Library {
        constructor() {
            this.shelfs = [];
        }

        addShelf(id, genre) {
            let shelfPresent = this.shelfs.find(x => x.id === id);
            if (!shelfPresent) {
                this.shelfs.push(new Shelf(id, genre));
            }
        }

        addBook(title, author, genre) {
            let shelf = this.shelfs.find(x => x.genre === genre);
            if (shelf) {
                shelf.books.push(new Book(title, author, genre));
            }
        }

        sortShelves() {
            this.shelfs.sort((a, b) => b.booksCount - a.booksCount);
        }

        print() {
            this.sortShelves();
            this.shelfs.forEach(shelf => {
                console.log(`${shelf.id} ${shelf.genre}: ${shelf.booksCount}`);
                shelf.sortBooks();
                shelf.books.forEach(book => {
                    console.log(`--> ${book.title}: ${book.author}`);
                });
            });
        }
    }

    class Shelf {
        constructor(id, genre) {
            this.id = id;
            this.genre = genre;
            this.books = []
        }

        get booksCount() {
            return this.books.length;
        }

        sortBooks() {
            this.books.sort((a, b) => a.title.localeCompare(b.title));
        }
    }

    class Book {
        constructor(title, author, genre) {
            this.title = title;
            this.author = author;
            this.genre = genre;
        }
    }

    let lib = new Library();

    data.forEach(entry => {
        if (entry.includes(' -> ')) {
            // Add new shelf:
            let newShelfID = entry.split(' -> ')[0];
            let newShelfGenre = entry.split(' -> ')[1];

            lib.addShelf(newShelfID, newShelfGenre);
        } else {
            // Add new book:
            let newBookTitle = entry.split(': ')[0];
            let newBookAuthor = entry.split(': ')[1].split(', ')[0];
            let newBookGenre = entry.split(': ')[1].split(', ')[1];

            lib.addBook(newBookTitle, newBookAuthor, newBookGenre);
        }
    });

    lib.print();
}


bookShelf(['1 -> history', '1 -> action', 'Death in Time: Criss Bell, mystery', '2 -> mystery', '3 -> sci-fi', 'Child of Silver: Bruce Rich, mystery', 'Hurting Secrets: Dustin Bolt, action', 'Future of Dawn: Aiden Rose, sci-fi', 'Lions and Rats: Gabe Roads, history', '2 -> romance', 'Effect of the Void: Shay B, romance', 'Losing Dreams: Gail Starr, sci-fi', 'Name of Earth: Jo Bell, sci-fi', 'Pilots of Stone: Brook Jay, history']);
// 3 sci-fi: 3
// --> Future of Dawn: Aiden Rose
// --> Losing Dreams: Gail Starr
// --> Name of Earth: Jo Bell
// 1 history: 2
// --> Lions and Rats: Gabe Roads
// --> Pilots of Stone: Brook Jay
// 2 mystery: 1
// --> Child of Silver: Bruce Rich

console.log('-------------------------------------');

bookShelf(['1 -> mystery', '2 -> sci-fi',
    'Child of Silver: Bruce Rich, mystery',
    'Lions and Rats: Gabe Roads, history',
    'Effect of the Void: Shay B, romance',
    'Losing Dreams: Gail Starr, sci-fi',
    'Name of Earth: Jo Bell, sci-fi']
);
// 2 sci-fi: 2
// --> Losing Dreams: Gail Starr
// --> Name of Earth: Jo Bell
// 1 mystery: 1
// --> Child of Silver: Bruce Rich
