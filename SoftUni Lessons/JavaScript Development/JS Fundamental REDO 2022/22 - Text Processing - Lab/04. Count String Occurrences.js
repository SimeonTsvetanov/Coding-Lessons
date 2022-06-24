function countStringOccurrences (text, word) {
    // MasK
    let length = text.split(' ').filter(w => w === word).length;
    console.log(length);
}

countStringOccurrences('This is a word and it also is a sentence',
    'is'
);  // 2