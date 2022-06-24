function modernTimesOfHashTag (text) {
    // MasK
    function onlyLetters(str) {
        return /^[a-zA-Z]+$/.test(str);
    }

    text.split(' ').forEach(word => {
        if (word[0] === '#') {
            let special = word.replace('#', '')
            if (onlyLetters(special)) {
                console.log(special);
            }
        }
    });
}

modernTimesOfHashTag('Nowadays everyone uses # to tag a #special word in #socialMedia');
// special
// socialMedia
