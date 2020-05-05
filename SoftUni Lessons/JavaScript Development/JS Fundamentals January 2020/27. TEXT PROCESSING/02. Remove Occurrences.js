function removeOccurrences(word, text) {
    // Mask
    while (true) {
        if (text.includes(word)) {
            text = text.replace(word, '')
        } else {
            break;
        }
    }

    console.log(text);
}

removeOccurrences('ice', 'kicegiciceeb');  // Should return:
// kgb
