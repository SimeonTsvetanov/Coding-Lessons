function revealWords (words, text) {
    // MasK
    text = text.split(' ');
    words = words.split(', ');
    words.forEach(word => {
        let coded = '*'.repeat(word.length);
        for (let w of text) {
            if (w === coded) {
                text[text.indexOf(coded)] = word;
                break;
            }
        }
    });

    console.log(text.join(' '));
}

revealWords('great',
    'softuni is ***** place for learning new programming languages'
);

// softuni is great place for learning new programming languages

revealWords('great, learning',
    'softuni is ***** place for ******** new programming languages'
);

// softuni is great place for learning new programming languages