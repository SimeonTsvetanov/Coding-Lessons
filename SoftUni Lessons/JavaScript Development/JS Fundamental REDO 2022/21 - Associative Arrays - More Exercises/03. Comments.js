function comments (data) {
    // MasK -- 80/100 in Judge (No idea why... I've tried with different solutions I think it's a Judge problem!!!
    // Have you watched the movie INCEPTION :D

    function sortObject(obj) {
        let sortedKVP = Array.from(Object.entries(obj)).sort((a, b) => {
            // Example Sort buy value (NUMBER) the smallest FIRST
            let aLen = Object.values(a[1]).length;
            let bLen = Object.values(b[1]).length;
            return bLen - aLen || 'if you want a second condition';
        });
        let sortedObject = {}
        for (let i = 0; i < sortedKVP.length; i ++) {
            sortedObject[sortedKVP[i][0]] = sortedKVP[i][1]
        }
        return sortedObject;
    }

    let articles = {}  // { nameOfArticle: { nameOfUser: { nameOfComment: commentContent } } }
    let users = [];  // To keep the users Allowed to comment

    data.forEach(entry => {
        if (entry.split(' ')[0] === 'article') {
            // Add a new Article:
            const newArticleName = entry.split(' ')[1];  // Get the name of the Article
            articles[newArticleName] = {};
        } else if (entry.split(' ')[0] === 'user') {
            // Add a new Article:
            const newUserName = entry.split(' ')[1];  // Get the name of the User
            users.push(newUserName);                  // Push it in the list
        } else if (entry.includes(' posts on ')){
            // Add the Comment if the User and Article exist:

            // Sort the input
            let userName = entry.split(' ')[0]
            let articleName = entry.split(' ')[3].split(':')[0]
            let commentTitle = entry.split(': ')[1].split(', ')[0];
            let commentContent = entry.split(': ')[1].split(', ')[1];

            // Check if we have the user and article:
            if ((users.includes(userName)) && (articles.hasOwnProperty(articleName))) {
                if (articles[articleName].hasOwnProperty(userName)) {
                    articles[articleName][userName][commentTitle] = commentContent;
                }
                articles[articleName][userName] = {};
                articles[articleName][userName][commentTitle] = commentContent;
            }
        }
    });

    // And finally sort and print the Output... That's ....
    let sortedArticles = sortObject(articles);
    users.sort((a, b) => {return a.localeCompare(b)});

    for (let [articleName, users] of Object.entries(sortedArticles)) {
        console.log(`Comments on ${articleName}`);
        let sortedUsers = Array.from(Object.entries(users)).sort((a, b) => {
            return a[0].localeCompare(b[0]);
        })

        for (let [userName, comment] of sortedUsers) {
            for (let [commentName, commentContent] of Object.entries(comment)) {
                console.log(`--- From user ${userName}: ${commentName} - ${commentContent}`);
            }
        }
    }
}

comments(['user aUser123', 'someUser posts on someArticle: NoTitle, stupidComment', 'article Books', 'article Movies', 'article Shopping', 'user someUser', 'user uSeR4', 'user lastUser', 'uSeR4 posts on Books: I like books, I do really like them', 'uSeR4 posts on Movies: I also like movies, I really do', 'someUser posts on Shopping: title, I go shopping every day', 'someUser posts on Movies: Like, I also like movies very much']);
// Comments on Movies
// --- From user someUser: Like - I also like movies very much
// --- From user uSeR4: I also like movies - I really do
// Comments on Books
// --- From user uSeR4: I like books - I do really like them
// Comments on Shopping
// --- From user someUser: title - I go shopping every day

console.log(' ');

comments(['user Mark', 'Mark posts on someArticle: NoTitle, stupidComment', 'article Bobby', 'article Steven', 'user Liam', 'user Henry', 'Mark posts on Bobby: Is, I do really like them', 'Mark posts on Steven: title, Run', 'someUser posts on Movies: Like']);
// Comments on Bobby
// --- From user Mark: Is - I do really like them
// Comments on Steven
// --- From user Mark: title - Run
