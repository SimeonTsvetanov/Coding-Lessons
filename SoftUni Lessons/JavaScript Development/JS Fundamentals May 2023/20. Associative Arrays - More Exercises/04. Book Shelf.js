function mask (params) {
    // MASK
    class Shelf {
        constructor(id, genre) {
            this.id = id;
            this.genre = genre;
            this.books = [];
        }

        get count() {
            return this.books.length;
        }

        addBook(book) {
            if (book.genre === this.genre) {
                this.books.push(book);
            }
        }

        get print() {
            return `${this.id} ${this.genre}: ${this.count}`
        }
    }

    class Book {
        constructor(title, author, genre) {
            this.title = title;
            this.author = author;
            this.genre = genre;
        }

        get print() {
            return `--> ${this.title}: ${this.author}`;
        }
    }

    let shelves = [];

    params.forEach(param => {
        if (param.includes(' -> ')) {
            // New Shelf
            let shelfId = param.split(' -> ')[0];
            let shelfGenre = param.split(' -> ')[1];

            let present = shelves.find(x => (x.id === shelfId));
            if (!present) {
                shelves.push(new Shelf(shelfId, shelfGenre));
            }
        } else {
            // New Book
            let bookTitle = param.split(': ')[0];
            let bookAuthor = param.split(': ')[1].split(', ')[0];
            let bookGenre = param.split(': ')[1].split(', ')[1];

            let present = shelves.find(x => (x.genre === bookGenre));
            if (present) {
                present.addBook(new Book(bookTitle, bookAuthor, bookGenre));
            }
        }
    });

    for (let shelf of shelves.sort((a, b) => b.count - a.count)) {
        console.log(shelf.print);
        for (let book of shelf.books.sort((a, b) => a.title.localeCompare(b.title))) {
            console.log(book.print);
        }
    }
}


mask(['1 -> mystery', '2 -> sci-fi',
'Child of Silver: Bruce Rich, mystery',
'Lions and Rats: Gabe Roads, history',
'Effect of the Void: Shay B, romance',
'Losing Dreams: Gail Starr, sci-fi',
'Name of Earth: Jo Bell, sci-fi']);
// 2 sci-fi: 2
// --> Losing Dreams: Gail Starr
// --> Name of Earth: Jo Bell
// 1 mystery: 1
// --> Child of Silver: Bruce Rich

console.log('-------------------------------------');

mask(['1 -> history', '1 -> action', 'Death in Time: Criss Bell, mystery', '2 -> mystery', '3 -> sci-fi', 'Child of Silver: Bruce Rich, mystery', 'Hurting Secrets: Dustin Bolt, action', 'Future of Dawn: Aiden Rose, sci-fi', 'Lions and Rats: Gabe Roads, history', '2 -> romance', 'Effect of the Void: Shay B, romance', 'Losing Dreams: Gail Starr, sci-fi', 'Name of Earth: Jo Bell, sci-fi', 'Pilots of Stone: Brook Jay, history']);
// 3 sci-fi: 3
// --> Future of Dawn: Aiden Rose
// --> Losing Dreams: Gail Starr
// --> Name of Earth: Jo Bell
// 1 history: 2
// --> Lions and Rats: Gabe Roads
// --> Pilots of Stone: Brook Jay
// 2 mystery: 1
// --> Child of Silver: Bruce Rich


