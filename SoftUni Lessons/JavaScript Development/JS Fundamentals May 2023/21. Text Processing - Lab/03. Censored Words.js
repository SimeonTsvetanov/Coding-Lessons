function mask (text, word) {
    // MASK
    while (text.includes(word)) {
        text = text.replace(word, Array(word.length + 1).join('*'));
    }
    console.log(text);
}

mask('A small sentence with some words', 'small');
// A ***** sentence with some words

console.log('-------------------------------------');

mask('Find the hidden word', 'hidden');
// Find the ****** word
