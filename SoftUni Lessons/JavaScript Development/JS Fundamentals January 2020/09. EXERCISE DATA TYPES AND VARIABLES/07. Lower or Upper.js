function lowerToUpper(char) {
    // Mask
    console.log(char === char.toLowerCase() ? 'lower-case' : 'upper-case');
}

lowerToUpper('L');  // Should return: upper-case

lowerToUpper('f');  // Should return: lower-case