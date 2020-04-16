function rightPlace(stringOne, char, stringTwo) {
    // Mask

    // Var 1:
    /*
    if (stringOne.replace('_', char) == stringTwo) {
        console.log('Matched');
    } else {
        console.log('Not Matched');
    }
    */
    
    // Var 2:
    console.log(stringOne.replace('_', char) == stringTwo ? 'Matched' : 'Not Matched');
}

rightPlace('Str_ng', 'I', 'Strong');  // Should return: Not Matched

rightPlace('Str_ng', 'i', 'String');  // Should return: Matched
