// Shortlink here: https://git.io/JfAoq

function pressHouse() {
    class Article {
        constructor(title, content) {
            this.title = title;
            this.content = content;
        }

        toString() {
            return `Title: ${this.title}\nContent: ${this.content}`
        }
    }
    class ShortReports extends Article{
        constructor(title, content, originalResearch) {
            super(title, content);
            this.originalResearch = originalResearch;  // Object with properties title and author
            this.comments = [];
        }

        get content() {
            return this._content
        }

        set content(value) {
            // As we create a short reports here we have a length limit for the content property
            // – it should be less than 150 symbols, otherwise throw an error with the next message:
            if (value.length < 150) { this._content = value; }
            else { throw new Error(`Short reports content should be less then 150 symbols.`); }
        }

        get originalResearch() {
            return this._originalResearch;
        }

        set originalResearch(object) {
            // The property should have the both required properties , otherwise throw error with this message:
            if (Object.keys(object).length === 2 && object.hasOwnProperty('title') && object.hasOwnProperty('author')) {
                this._originalResearch = object;
            } else { throw new Error(`The original research should have author and title.`); }
        }

        addComment(comment) {
            // This function should receive single comment like string,
            // add it to the comments array and return a message:
            // "The comment is added."
            this.comments.push(comment);
            return "The comment is added.";
        }

        toString() {
            // Apparently the output result sort is more important then the classes:
            // SoftUni stuff...

            let result = super.toString();
            result += `\nOriginal Research: ${this.originalResearch.title} by ${this.originalResearch.author}`;
            if (this.comments.length > 0) {
                result += '\nComments:\n';
                result += this.comments.join('\n');
            }
            return result;
        }

    }
    class BookReview extends Article {
        constructor(title, content, book) {
            super(title, content);
            this.book = book;  // object with properties name and author
            this.clients = []  // – array of objects,
        }

        addClient(clientName, orderDescription) {
            // This function should receive clientName and orderDescription as strings.
            // Here you should check our clients array and if we already
            // have this order from the same client throw error with next message:
            this.clients.map(client => {
                if (client.name === clientName) {
                    throw new Error(`This client has already ordered this review.`);
                }
            });

            //Otherwise we add our client object into the clients array and return a message:
            // let client = {name: clientName, orderDescription: orderDescription};
            let client = {name: clientName, order: orderDescription};
            this.clients.push(client);
            return `${clientName} has ordered a review for ${this.book.name}`;
        }

        toString() {
            let result = super.toString();
            result += `\nBook: ${this.book.name}`;
            if (this.clients.length > 0) {
                result += `\nOrders:`;
                this.clients.map(client => {
                    result += `\n${client.name} - ${client.order}.`
                });
            }
            return result;
        }
    }
    return {
        Article,
        ShortReports,
        BookReview,
    }
}

let classes = pressHouse();
let lorem = new classes.Article("Lorem", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce non tortor finibus, facilisis mauris vel…");
console.log(lorem.toString());

console.log('---------------------------------------------------------------------------------------------------');

let short = new classes.ShortReports(
    "SpaceX and Javascript",
    "Yes, its damn true.SpaceX in its recent launch Dragon 2 Flight has used a technology based on Chromium and Javascript. What are your views on this ?",
    { title: "Dragon 2", author: "wikipedia.org" }
    );
console.log(short.addComment("Thank god they didn't use java."));
short.addComment("In the end JavaScript's features are executed in C++ — the underlying language.");
console.log(short.toString());

console.log('---------------------------------------------------------------------------------------------------')

let book = new classes.BookReview("The Great Gatsby is so much more than a love story", "The Great Gatsby is in many ways similar to Romeo and Juliet, yet I believe that it is so much more than just a love story. It is also a reflection on the hollowness of a life of leisure. ...", { name: "The Great Gatsby", author: "F Scott Fitzgerald" });
console.log(book.addClient("The Guardian", "100 symbols"));
console.log(book.addClient("Goodreads", "30 symbols"));

console.log(book.toString());
