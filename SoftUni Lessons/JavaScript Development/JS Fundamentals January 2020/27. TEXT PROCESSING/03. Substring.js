function substring(text, index, count) {
    // Mask
    // The cheat method:
    // console.log(text.split('').splice(index, count).join(''));
    // But even better:
    console.log(text.substr(index, count));
}

substring("ASentance", 1, 8);  // Should return:
// Sentance
