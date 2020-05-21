function biggestElement(array) {
    // Mask
    console.log(Math.max(...array.flat()));
}

biggestElement([[20, 50, 10], [8, 33, 145]]);  // Should return: 145

biggestElement([[3, 5, 7, 12], [-1, 4, 33, 2], [8, 3, 0, 4]]);  // Should return: 33