function stringSubstring (word, text) {
    // MasK
    let wordFound = undefined;

    text.split(' ').forEach(w => {
        if (w.toLowerCase() === word.toLowerCase()) {
            wordFound = w.toLowerCase();
        }
    });

    wordFound ? console.log(wordFound) : console.log(`${word} not found!`);
}

stringSubstring('javascript',
    'JavaScript is the best programming language'
);
// javascript

stringSubstring('python',
    'JavaScript is the best programming language'
);
// python not found!