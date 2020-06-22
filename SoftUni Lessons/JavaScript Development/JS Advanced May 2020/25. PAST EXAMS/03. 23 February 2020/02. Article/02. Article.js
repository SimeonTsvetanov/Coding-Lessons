// Shortlink here: https://git.io/JfAPf

class Article {
    constructor(title, creator) {
        this.title = title;        // string
        this.creator = creator;    // string
        this._comments = [];       // private property (empty array by default)
        this._likes = [];          // private property (empty array by default)
    }

    get likes () {
        // This function should print the likes in the following format:
        let message = '';
        this._likes.length === 0 ? message = `${this.title} has 0 likes` : 'ass';
        this._likes.length === 1 ? message = `${this._likes[0]} likes this article!` : 'pass';
        this._likes.length > 1 ? message = `${this._likes[0]} and ${this._likes.length - 1} others like this article!` : 'or gas';
        return message;
    }

    like(username) {
        // This function should increase the likes of the article And return a message or gives an error.

        // If the username, has already liked the article, an error with the following message should be thrown:
        if (this._likes.includes(username)) { throw new Error(`You can\'t like the same article twice!`); }
        // If this user is the creator of the article, an error with the following message should be thrown:
        else if (username === this.creator) { throw new Error(`You can't like your own articles!`); }
        // Otherwise, the following message should be returned:
        this._likes.push(username);  //  Add the username to the likes list.
        return `${username} liked ${this.title}!`;
    }

    dislike(username) {
        // This function should decrease the likes of the article.

        // If the username, didn't like the article in the first place, an error with the following message should be thrown:
        if (!(this._likes.includes(username))) { throw new Error(`"You can't dislike this article!"`); }

        // Otherwise, the following message should be returned:
        this._likes = this._likes.filter(user => user !== username);  // Remove it from the likes list!
        return `${username} disliked ${this.title}`;
    }

    comment(username, content, id) {
        // This function should make a new comment or reply to a comment with a given id.

        if (id === undefined || !(this._comments.some((comment) => comment.id === id))) {
            //	If the given id is equal to undefined or there is not a comment with that id,
            // you should make a new comment and add it to the comments array.
            // Every comment should have an id (1, 2, 3 ...) which represents the order the comments are submitted.
            // If the comment is made successfully, the following message should be returned:
            let newId; this._comments.length === 0 ? newId = 1 : newId = this._comments.length + 1;
            // Comments should have the following structure:
            this._comments.push({id: newId, username: username, content: content, replies: [],});
            return `${username} commented on ${this.title}`;
        } else if (this._comments.some((comment) => comment.id === id)){
            // If there is a comment with the given id, you should add a reply to it.
            // The reply should have an id (1.1, 1.2 ...) constructed from the id of the comment
            // and the order in which the replies are submitted.
            // If the reply is made successfully the following message should be returned:
            let returnMessage = '';
            this._comments.map(comment => {
                if (comment.id === id) {
                    let replyNewId;
                    comment.replies.length === 0
                        ? replyNewId = `${comment.id}.1`
                        : replyNewId = `${comment.id}.${comment.replies.length + 1}`;
                    // Replies should have the following structure:
                    comment.replies.push({id: replyNewId, username: username, content: content});
                    returnMessage = `You replied successfully`;
                }
            });
            return returnMessage;
        }
    }

    toString(sortingType) {
        // This function should print the article information in the following format:

        let result = `Title: ${this.title}\nCreator: ${this.creator}\nLikes: ${this._likes.length}\nComments:`;

        let sortingTypes = {
            'asc': (a, b) => a.id - b.id,                                // Should be sorted by id in ascending order!
            'desc': (a, b) => b.id - a.id,                               // Should be sorted by id in descending order!
            'username': (a, b) => a.username.localeCompare(b.username),  // Should be sorted by username in ascending!
        };

        let sorting = sortingTypes[sortingType];

        this._comments.sort(sorting).map(currentElement => {
            result += `\n-- ${currentElement.id}. ${currentElement.username}: ${currentElement.content}`;
            if (currentElement.replies.length > 0) {
                currentElement.replies.sort(sorting).map(currentReply => {
                    result += `\n--- ${currentReply.id}. ${currentReply.username}: ${currentReply.content}`;
                });
            }
        });

        return result;
    }
}

let art = new Article("My Article", "Anny");
art.like("John");
console.log(art.likes);  // John likes this article!
art.dislike("John");
console.log(art.likes);  // My Article has 0 likes

console.log();

art.comment("Sammy", "Some Content");
console.log(art.comment("Ammy", "New Content"));  // Ammy commented on My Article
art.comment("Zane", "Reply", 1);
art.comment("Jessy", "Nice :)");
console.log(art.comment("SAmmy", "Reply@", 1));  // You replied successfully

console.log();

console.log(art.toString('username'));

console.log();

art.like("Zane");
console.log(art.toString('desc'));
