function countStringOccurrences(text, word) {
    // Mask
    let count = 0
    text.split(' ').forEach(x => word === x ? count += 1 : 'pass');
    console.log(count);
}

countStringOccurrences("This is a word and it also is a sentence", "is");
// Should return: 2
