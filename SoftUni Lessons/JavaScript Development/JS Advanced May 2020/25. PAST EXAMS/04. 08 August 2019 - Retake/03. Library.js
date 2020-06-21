class Library {
    constructor(libraryName) {
        this.libraryName = libraryName;       // should be the same as the received libraryName
        this.subscribers = [];                // Empty Array
        this.subscriptionTypes = {            // object with properties normal, special and vip
            normal: libraryName.length,       // Normal: length of the libraryName
            special: libraryName.length * 2,  // Special: libraryName multiplied by 2
            vip: Number.MAX_SAFE_INTEGER,     // VIP: unlimited amount of books
        }
    }
    subscribe(name, type) {
        let currentSubscriber;
        // If the given subscription type is not normal, special or vip, a new error should be thrown:
        if (!(type === 'normal' || type === 'special' || type === 'vip')) {
            throw new Error(`The type ${type} is invalid`);
        }

        // If there is a person with that name in the subscribers list,
        // you should just change his subscription type with the given type.
        this.subscribers.map(subscriber => {
            if (name === subscriber.name) {
                subscriber.type = type;
                currentSubscriber = subscriber;
            }
        });

        // If the person is not subscribed, you should make new subscriber object with properties
        // name (the subscriber name) / type (the subscription type) / books (an empty array by default)
        // And add it to the library subscribers' array.
        if (!currentSubscriber) {
            currentSubscriber = {name: name, type: type, books: []};
            this.subscribers.push(currentSubscriber)
        }

        //This function should return the current subscriber.
        return currentSubscriber;
    }
    unsubscribe(name) {
        // This function receives 1 parameter name
        // and should unsubscribe an already subscribed person in the library
        // (remove the person with the given name from the subscriber's property).

        let notSubscribed = true;  // Flag to check if we need throw an Error later

        this.subscribers.map((person, index) => {
            // If subscribers  property contains a person with the given name,
            // that person should be removed from the array.
            if (person.name === name) {
                this.subscribers.splice(index, 1);
                notSubscribed = false;  // Change the flag.
            }
        });

        if (notSubscribed) {
            // If there is no subscriber with that name, a new error should be thrown with the following message:
            throw new Error(`There is no such subscriber as ${name}`);
        }

        // This function should return the library's subscribers list
        return this.subscribers;
    }
    receiveBook(subscriberName, bookTitle, bookAuthor) {
        let searchedSubscriber;
        this.subscribers.map(subscriber => {
            if (subscriber.name === subscriberName) {
                searchedSubscriber = subscriber;
                // If there is a subscriber with that name you should check his subscription type
                let limit = this.subscriptionTypes[subscriber.type];
                // If his subscription type allows him to receive more book
                // you should add a new book object with properties title and author to his books array
                if (subscriber.books.length < limit) {
                    let book = {title: bookTitle, author: bookAuthor};
                    subscriber.books.push(book);
                } else {
                    // Otherwise a new error should be thrown, with the following message:
                    throw new Error(`You have reached your subscription limit ${limit}!`);
                }
            }
        });

        if (!searchedSubscriber) {
            // If there is no such subscriber in the subscriber's array,
            // a new error should be thrown with the following message:
            throw new Error(`There is no such subscriber as ${subscriberName}`);
        }

        // This function should return the subscriber with the given name:
        return searchedSubscriber;
    }
    showInfo() {
        // This function should return a string with  all the subscribers with their books joined by (", ")

        // If the subscriber's property in the Library is empty just return the following string:
        if (this.subscribers.length <= 0) {
            return `${this.libraryName} has no information about any subscribers`;
        }

        // Else:
        let result = '';
        this.subscribers.map(sub => {
            result += `Subscriber: ${sub.name}, Type: ${sub.type}\nReceived books: `;
            result += sub.books.map(book => `${book.title} by ${book.author}`).join(', ');
            result += '\n'
        });
        return result;
    }
}

let lib = new Library('Lib');
lib.subscribe('Peter', 'normal');
lib.subscribe('John', 'special');
lib.receiveBook('John', 'A Song of Ice and Fire', 'George R. R. Martin');
lib.receiveBook('Peter', 'Lord of the rings', 'J. R. R. Tolkien');
lib.receiveBook('John', 'Harry Potter', 'J. K. Rowling');
console.log(lib.showInfo());



