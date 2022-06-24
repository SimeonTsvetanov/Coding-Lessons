function substring (string, start, end) {
    // MasK
    console.log(string.split('').splice(start, end).join(''));
}

substring('ASentence', 1, 8);