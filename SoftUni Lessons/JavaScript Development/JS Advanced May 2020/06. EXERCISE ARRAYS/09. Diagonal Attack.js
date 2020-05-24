function diagonalAttack(matrix) {
    // Mask

    // Set the rows to be Arrays of Numbers
    matrix = matrix.map(row => row.split(' ').map(Number));

    // Main Variables:
    let diagonalCoordinates = [];
    let left = 0;
    let right = 0;

    // Set the Diagonal Sums and Coordinates:
    for (let i = 0; i < matrix.length; i++) {
        left += matrix[i][i];
        right += matrix[i][matrix.length - i - 1];
        diagonalCoordinates.push(`${i} ${i}`);
        diagonalCoordinates.push(`${i} ${matrix.length - i - 1}`);
    }

    // Check for Magic:
    if (left === right) {
        for (let row = 0; row < matrix.length; row++) {
            for (let col = 0; col < matrix.length; col++) {
                let coordinate = `${row} ${col}`;
                if (!(diagonalCoordinates.includes(coordinate))) {
                    matrix[row][col] = left;
                }
            }
        }
    }

    // Print the Matrix:
    matrix.map(row => console.log(row.join(' ')));
}

diagonalAttack([
    '5 3 12 3 1',
    '11 4 23 2 5',
    '101 12 3 21 10',
    '1 4 5 2 2',
    '5 22 33 11 1'
]);  // Should return:
// 5 15 15 15 1
// 15 4 15 2 15
// 15 15 3 15 15
// 15 4 15 2 15
// 5 15 15 15 1

diagonalAttack([
    '1 1 1',
    '1 1 1',
    '1 1 0'
]);  // Should return:
// 1 1 1
// 1 1 1
// 1 1 0
