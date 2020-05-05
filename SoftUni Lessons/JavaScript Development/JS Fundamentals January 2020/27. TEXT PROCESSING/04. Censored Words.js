function censoredWords(text, word) {
    // Mask
    let replacedText = text;
    while (replacedText.includes(word)) {
        replacedText = replacedText.replace(word, '*'.repeat(word.length));
    }
    console.log(replacedText);
}

censoredWords("A small sentence with some words", "small");
// Should return: A ***** sentence with some words
