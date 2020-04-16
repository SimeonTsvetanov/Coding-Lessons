function integerAndFloat(numOne, numTwo, numThree) {
    // Mask
    let total = numOne + numTwo + numThree;
    let intOrDecimal = total % 1 === 0 ? 'Integer' : 'Float';
    console.log(`${total} - ${intOrDecimal}`);
}

integerAndFloat(9, 100, 1.1);  // Should return:
// 110.1 - Float

integerAndFloat(100, 200, 303);  // Should return:
// 603 - Integer
