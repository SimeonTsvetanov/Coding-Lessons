function sumOfDigits(num) {
    // Mask
    let digits = String(num).split('').map(x => Number(x)).reduce((a, b) => a + b);
    console.log(digits);
}

sumOfDigits(245678);  // Should return: 32

sumOfDigits(97561);  // Should return: 28
