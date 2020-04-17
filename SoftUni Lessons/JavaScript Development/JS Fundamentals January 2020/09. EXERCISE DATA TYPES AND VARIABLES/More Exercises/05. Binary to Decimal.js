function binaryToDecimal(binary) {
    // Mask
    let digit = parseInt(binary, 2);
    console.log(digit);
}

binaryToDecimal('00001001');  // Should return: 9

binaryToDecimal('11110000');  // Should return: 240