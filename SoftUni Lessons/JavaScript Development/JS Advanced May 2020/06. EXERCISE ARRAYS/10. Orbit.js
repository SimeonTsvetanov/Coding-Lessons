// Not included in final score
function orbit([rows, cols, starRow, starCol]) {

    let matrix = [];
    for(let i=0; i<rows; i++) {
        matrix.push([]);
    }
    console.log(matrix);

    for(let row = 0; row< rows; row++) {
        for(let col=0; col<cols; col++) {
            matrix[row][col] = Math.max(Math.abs(row - starRow), Math.abs(col - starCol)) + 1;
        }
    }

    console.log(matrix.map(row => row.join(" ")).join("\n"));
}

orbit([4, 4, 0, 0]);  // Should return:
// 1 2 3 4
// 2 2 3 4
// 3 3 3 4
// 4 4 4 4

orbit([5, 5, 2, 2]);  // Should return:
// 3 3 3 3 3
// 3 2 2 2 3
// 3 2 1 2 3
// 3 2 2 2 3
// 3 3 3 3 3