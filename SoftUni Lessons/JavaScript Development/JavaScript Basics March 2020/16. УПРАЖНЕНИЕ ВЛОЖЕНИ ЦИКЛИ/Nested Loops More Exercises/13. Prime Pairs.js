function primePairs(input) {
    // Mask
    let first = Number(input.shift());
    let second = Number(input.shift());
    let diffFirst = Number(input.shift());
    let diffSecond = Number(input.shift());

    let primeNumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];

    for (let one = first; one <= first + diffFirst; one += 1) {
        for (let two = second; two <= second + diffSecond; two += 1) {
            if (primeNumbers.includes(one) && primeNumbers.includes(two)) {
                console.log(`${one}${two}`);
            }
        }
    }
    
}

primePairs([10, 20, 5, 5]);  // Should return:
// 1123
// 1323

primePairs([10, 30, 9, 6]);  // Should return:
// 1131
// 1331
// 1731
// 1931
