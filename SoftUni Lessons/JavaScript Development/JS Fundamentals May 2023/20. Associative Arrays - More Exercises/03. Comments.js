function mask (params) {
    // MASK - Judge 80/100 ...
    let articles = {};
    let users = [];

    params.forEach(param => {
        if (param.includes('user ')) {
            let user = param.split('user ')[1];
            users.push(user);
        } else if (param.includes('article ')) {
            let article = param.split('article ')[1];
            if (!(article in articles)) {
                articles[article] = {};
            }
        } else {
            // "{username} posts on {article name}: {comment title}, {comment content}"
            let user = param.split(": ")[0].split(" posts on ")[0];
            let article = param.split(": ")[0].split(" posts on ")[1];
            let c_title = param.split(": ")[1].split(", ")[0];
            let c_content = param.split(": ")[1].split(", ")[1];

            if (users.includes(user) && (article in articles)) {
                articles[article][user] = {};
                articles[article][user][c_title] = c_content;
            }
        }
    });

    for (let [article, comments] of Object.entries(articles)
        .sort((a, b) => {
            return Object.entries(b[1]).length - Object.values(a[1]).length;
        })) {
        console.log(`Comments on ${article}`);
        for (let [user, comment] of Object.entries(comments)
            .sort((a, b) => {
                return a[0].localeCompare(b[0]);
            })) {
            console.log(`--- From user ${user}: ${Object.keys(comment)} - ${Object.values(comment)}`);
            // console.log(user, comment);
        }
    }
}

mask(['user aUser123', 'someUser posts on someArticle: NoTitle, stupidComment', 'article Books',
'article Movies', 'article Shopping', 'user someUser', 'user uSeR4', 'user lastUser', 'uSeR4 posts on Books: I like books, I do really like them', 'uSeR4 posts on Movies: I also like movies, I really do', 'someUser posts on Shopping: title, I go shopping every day',
'someUser posts on Movies: Like, I also like movies very much']);
// Comments on Movies
// --- From user someUser: Like - I
// also like movies very much
// --- From user uSeR4: I also like
// movies - I really do
// Comments on Books
// --- From user uSeR4: I like books -
// I do really like them
// Comments on Shopping
// --- From user someUser: title - I go
// shopping every day

console.log('-------------------------------------');

mask(['user Mark', 'Mark posts on someArticle: NoTitle, stupidComment', 'article Bobby',
'article Steven', 'user Liam', 'user Henry', 'Mark posts on Bobby: Is, I do really like them', 'Mark posts on Steven: title, Run', 'someUser posts on Movies: Like']);
// Comments on Bobby
// --- From user Mark: Is - I do really
// like them
// Comments on Steven
// --- From user Mark: title - Run
