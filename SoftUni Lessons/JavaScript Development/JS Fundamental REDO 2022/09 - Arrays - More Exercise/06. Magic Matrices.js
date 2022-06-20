function magicMatrix(matrix) {
    // Mask
    let result = [];
    for (let row = 0; row < matrix.length; row++) {
        result.push(matrix[row].map(Number).reduce((a, b) => a + b, 0));
    }
    let resultTwo = matrix.reduce(function (r, a) {
        a.forEach(function (b, i) {
            r[i] = (r[i] || 0) + b;
        });
        return r;
    }, []);
    console.log(new Set(result.concat(resultTwo)).size === 1);
}

magicMatrix([[4, 5, 6],
    [6, 5, 4],
    [5, 5, 5]]
);  // true

magicMatrix([[11, 32, 45],
    [21, 0, 1],
    [21, 1, 1]]
);  // false

magicMatrix([[1, 0, 0],
    [0, 0, 1],
    [0, 1, 0]]
);  // true