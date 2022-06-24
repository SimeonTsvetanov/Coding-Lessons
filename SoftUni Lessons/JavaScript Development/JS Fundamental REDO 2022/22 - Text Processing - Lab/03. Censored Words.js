function censoredWords (text, word) {
    // MasK
    while (text.includes(word)) {
        text = text.replace(word, '*'.repeat(word.length));
    }
    console.log(text);
}

censoredWords('A small sentence with some words', 'small');