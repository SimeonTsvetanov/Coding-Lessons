function solveClasses() {
    class Article {
        constructor(title, content) {
            this.title = title;
            this.content = content;
        }

        toString() {
            return `Title: ${this.title}\nContent: ${this.content}`;
        }
    }

    class ShortReports extends Article {
        constructor(title, content, originalResearch) {
            super(title, content);
            this.originalResearch = originalResearch;
            this.comments = [];
        }

        get content() {
            return this._content;
        }

        set content(value) {
            if (value.length >= 150) {
                throw new Error("Short reports content should be less then 150 symbols.");
            } else {
                this._content = value;
            }
        }

        get originalResearch() {
            return this._originalResearch;
        }

        set originalResearch(object) {
            if (object.hasOwnProperty('title') && object.hasOwnProperty('author')) {
                this._originalResearch = object;
            } else {
                throw new Error("The original research should have author and title.");
            }
        }

        addComment(comment) {
            this.comments.push(comment);
            return 'The comment is added.';
        }

        toString() {
            let result = super.toString();
            result += `\nOriginal Research: ${this.originalResearch.title} by ${this.originalResearch.author}`;
            if (this.comments.length > 0) {
                result += `\nComments:`;
                this.comments.map(comment => result += `\n${comment}`);
            }
            return result;
        }
    }

    class BookReview extends Article {
        constructor(title, content, book) {
            super(title, content);
            this.title = title;
            this.content = content;
            this.book = book;
            this.clients = [];
        }

        addClient(clientName, orderDescription) {
            this.clients.map(client => {
                if (client.name === clientName) {
                    throw new Error(`This client has already ordered this review.`);
                }
            });

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
                    result += `\n${client.name} - ${client.order}.`;
                });
            }
            return result;
        }
    }


    return {
        Article,
        ShortReports,
        BookReview
    }
}

let classes = solveClasses();
let lorem = new classes.Article("Lorem", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce non tortor finibus, facilisis mauris vel…");
console.log(lorem.toString());
let short = new classes.ShortReports("SpaceX and Javascript", "Yes, its damn true.SpaceX in its recent launch Dragon 2 Flight has used a technology based on Chromium and Javascript. What are your views on this ?", { title: "Dragon 2", author: "wikipedia.org" });
console.log(short.addComment("Thank god they didn't use java."))
short.addComment(`In the end JavaScript"s features are executed in C++ — the underlying language.`)
console.log(short.toString());
