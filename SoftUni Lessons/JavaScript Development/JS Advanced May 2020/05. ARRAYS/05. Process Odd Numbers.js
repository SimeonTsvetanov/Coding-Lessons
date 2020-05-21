function processOddNumbers(array = []) {
    // Mask
    console.log(array.filter((el, ind) => ind % 2 !== 0).map(element => element * 2).reverse().join(' '));
}

processOddNumbers([10, 15, 20, 25]);  // Should return: 50 30
processOddNumbers([3, 0, 10, 4, 7, 3]);  // Should return: 6 8 0
