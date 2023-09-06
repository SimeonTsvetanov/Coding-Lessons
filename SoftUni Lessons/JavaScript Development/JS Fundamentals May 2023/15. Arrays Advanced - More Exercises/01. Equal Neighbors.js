function mask (matrix) {
    // MASK
    let equalPairs = 0;

    // Check for horizontal pairs:
    matrix.forEach(row => {
        row.forEach((element, index) => {
            if (index + 1 < row.length) {
                if (element === row[index + 1]) {
                    equalPairs += 1;
                }
            }
        });
    });

    // Check for vertical pairs:
    matrix.forEach((row, index_row)=> {
        row.forEach((element, index_elemet) => {
            if (index_row + 1 < matrix.length) {
                if (element === matrix[index_row + 1][index_elemet]) {
                    equalPairs += 1;
                }
            }
        });
    });

    console.log(equalPairs);
}

mask([['2', '3', '4', '7', '0'],
['4', '0', '5', '3', '4'],
['2', '3', '5', '4', '2'],
['9', '8', '7', '5', '4']]);
// 1

console.log('-------------------------------------');

mask([['test', 'yo', 'yo',
'ho'],
['well', 'done', 'no',
'6'],
['not', 'done', 'yet',
'5']]);
// 2
