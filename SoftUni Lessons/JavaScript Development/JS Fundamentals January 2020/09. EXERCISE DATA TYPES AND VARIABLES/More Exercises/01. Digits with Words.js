function digitsWithWords(digit) {
    // Mask

    /*
    // Opiton 1:
    switch (digit) {
        case 'zero':
            digit = 0;
            break;
        case 'one':
            digit = 1;
            break;
        case 'two':
            digit = 2;
            break;
        case 'three':
            digit = 3;
            break;
        case 'four':
            digit = 4;
            break;
        case 'five':
            digit = 5;
            break;
        case 'six':
            digit = 6;
            break;
        case 'seven':
            digit = 7;
            break;
        case 'eight':
            digit = 8;
            break;
        case 'nine':
            digit = 9;
            break;
    }
    console.log(digit);
    */ 

    // And Opition 2:
    console.log({'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}[digit]);
}

digitsWithWords('nine');  // Should return: 9

digitsWithWords('two');  // Should return: 2