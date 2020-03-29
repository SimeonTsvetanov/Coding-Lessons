function oldBooks(data) {
    let searched = data.shift();
    let books = Number(data.shift());
    
    let book = 1;
    let found = false;
    while (book <= books) {
        if (searched === data.shift()) {
            console.log(`You checked ${book - 1} books and found it.`);
            found = true
            break;
        }
        book += 1;
    }
    if (!found) {
        console.log(`The book you search is not here!`);
        console.log(`You checked ${books} books.`);
    }
}


oldBooks(['Troy', '8', 'Stronger', 'Life Style', 'Troy']);
// Expected Output:
// You checked 2 books and found it.

oldBooks(['The Spot', '4', 'Hunger Games', 'Harry Potter', 'Torronto', 'Spotify']);
// Expected Output:
// The book you search is not here!
// You checked 4 books.
