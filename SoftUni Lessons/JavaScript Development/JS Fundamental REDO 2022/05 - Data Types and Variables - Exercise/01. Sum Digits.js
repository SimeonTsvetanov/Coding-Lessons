function sumOfDigits (...args) {
    // MasK
    let sum = args.shift()
        .toString()
        .split('')
        .map(Number)
        .reduce((a, b) => a + b);
    console.log(sum);
}

sumOfDigits(245678);
