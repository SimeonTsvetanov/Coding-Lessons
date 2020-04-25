function smallestTwoNumbers(array) {
    // Mask
    let smallestTwoIntegers = array
        .sort((a, b) => a - b)
        .slice(0, 2);
    console.log(...smallestTwoIntegers);
}

smallestTwoNumbers([30, 15, 50, 5]);  // Should return: 5 15

smallestTwoNumbers([3, 0, 10, 4, 7, 3]);  // Should return: 0 3