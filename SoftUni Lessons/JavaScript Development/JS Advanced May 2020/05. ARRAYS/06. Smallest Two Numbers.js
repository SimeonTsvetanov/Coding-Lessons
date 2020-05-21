function smallestTwoNumbers(array = []) {
    // Mask
    console.log(array.sort((a, b) => a - b).slice(0, 2).join(' '));
}

smallestTwoNumbers([30, 15, 50, 5]);  // Should return: 5 15

smallestTwoNumbers([3, 0, 10, 4, 7, 3]);  // Should return: 0 3
