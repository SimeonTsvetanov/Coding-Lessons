function replaceRepeatingChars (string) {
    // MasK
    let result = [];
    string.split('').forEach(letter => {
        if (result[result.length - 1] !== letter) {
            result.push(letter);
        }
    });

    console.log(result.join(''));
}

replaceRepeatingChars('aaaaabbbbbcdddeeeedssaa');