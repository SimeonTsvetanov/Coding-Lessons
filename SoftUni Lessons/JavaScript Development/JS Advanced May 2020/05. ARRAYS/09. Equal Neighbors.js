function equalNeighbors(matrix = []) {
    // Mask
    let neighbors = 0;

    for (let row = 0; row < matrix.length - 1; row++) {
        for (let col = 0; col < matrix[row].length; col++) {
            if (matrix[row][col] === matrix[row + 1][col]) {
                neighbors++;
            }
            if (matrix[row][col] === matrix[row][col + 1]) {
                neighbors++;
            }
            if (row === matrix.length - 2 && matrix[row + 1][col] === matrix[row + 1][col + 1]) {
                neighbors++;
            }
        }
    }
    console.log(neighbors);
}

equalNeighbors([
    ['2', '3', '4', '7', '0'],
    ['4', '0', '5', '3', '4'],
    ['2', '3', '5', '4', '2'],
    ['9', '8', '7', '5', '4']]
);  // Should return: 1

equalNeighbors([
    ['test', 'yes', 'yo', 'ho'],
    ['well', 'done', 'yo', '6'],
    ['not', 'done', 'yet', '5']]
);  // Should return: 2