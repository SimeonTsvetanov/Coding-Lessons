function reverseAnArrayOfNumbers(count, array) {
    // Mask
    console.log(array.slice(0, count).reverse().join(' '));
}

reverseAnArrayOfNumbers(3, [10, 20, 30, 40, 50]);  // Should return: 30 20 10

reverseAnArrayOfNumbers(4, [-1, 20, 99, 5]);  // Should return: 5 99 20 -1
