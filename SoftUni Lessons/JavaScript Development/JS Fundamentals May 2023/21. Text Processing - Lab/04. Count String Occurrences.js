function mask (text, word) {
    // MASK
    console.log((text.split(word).length - 1));
}

mask('This is a word and it also is a sentence', 'is');
// 2

console.log('-------------------------------------');

mask('softuni is great place for learning new programming languages', 'softuni' );
// 1
