function rosettaStone (data) {
    // MasK... What a task!

    // Create the Template:
    let template = [];
    let templateSize = +data.shift();
    for (let i = 0; i < templateSize; i++) {
        let temR = data.shift()
        template.push(temR.split(' ').map(Number));
    }

    // Create the Matrix:
    let matrix = [];
    data.forEach(row => {matrix.push(row.split(' ').map(Number))});

    // Crete Function that will Decode given sum to the correct Letter
    const decoder = (num) => {
        num = num % 27;
        return num === 0 ? ' ' : String.fromCharCode(num + 64);
    };

    // Function to check if given coordinates are in the matrix
    let cordsAreInTheMatrix = (m, r ,c) => {
        return (r >= 0 && r < m.length) && (c >= 0 && c < m[r].length);
    };

    for (let matrixRow = 0; matrixRow < matrix.length; matrixRow += template.length) {
        for (let matrixCol = 0; matrixCol < matrix[matrixRow].length; matrixCol += template[0].length) {
            // Starting index for the template to be place:
            for (let tempRow = 0; tempRow < template.length; tempRow++) {
                for (let tempCol = 0; tempCol < template[tempRow].length; tempCol++) {
                    let tempElement = template[tempRow][tempCol];

                    // Get the coordinates of the current element in the matrix:
                    let currentRow = matrixRow + tempRow;
                    let currentCol = matrixCol + tempCol;

                    // Check if they are in the matrix:
                    if (cordsAreInTheMatrix(matrix, currentRow, currentCol)) {
                        // Get the sum of the elements:
                        let sum = template[tempRow][tempCol] + matrix[currentRow][currentCol];
                        // Get the decoded letter and
                        // set it in the matrix:
                        matrix[currentRow][currentCol] = decoder(sum);
                    }
                }
            }
        }
    }

    console.log(matrix.flat().join(''));
}

rosettaStone([ '2',
    '59 36',
    '82 52',
    '4 18 25 19 8',
    '4 2 8 2 18',
    '23 14 22 0 22',
    '2 17 13 19 20',
    '0 9 0 22 22' ]
);
// I CAME I SAW I CONQUERED

console.log('---------------------------');

rosettaStone([ '2',
    '31 32',
    '74 37',
    '19 0 23 25',
    '22 3 12 17',
    '5 9 23 11',
    '12 18 10 22' ]
);
// WE COME IN PEACE

console.log('---------------------------');

rosettaStone(
    [ '1',
        '1 3 13',
        '12 22 14 13 25 0 4 24 23',
        '18 24 2 25 22 0 0 11 18',
        '8 25 6 26 8 23 13 4 14',
        '14 3 14 10 6 1 6 16 14',
        '11 12 2 10 24 2 13 24 0',
        '24 24 10 14 15 25 18 24 12',
        '4 24 0 8 4 22 19 22 14',
        '0 11 18 26 1 19 18 13 15',
        '8 15 14 26 24 14 26 24 14' ]
);
// MY NAME IS OZYMANDIAS KING OF KINGS LOOK ON MY WORKS YE MIGHTY AND DESPAIR