function diagonalSums(array) {
    // Mask
    let left = 0;
    let right = 0;
    for (let i = 0; i < array.length; i++) {
        left += array[i][i];
        right += array[i][array.length - i - 1];
    }
    console.log(left, right);
}

diagonalSums([
    [20, 40],
    [10, 60]
]);  // Should return: 80, 50

diagonalSums([
    [3, 5, 17],
    [-1, 7, 14],
    [1, -8, 89]
]);  // Should return: 99, 25