function mask (n) {
    // MASK
    let matrix = Array.from({
    // generate array of length n
    length: n
    // inside map function generate array of size n
    // and fill it with `n`
    }, () => new Array(n).fill(n));

    matrix.forEach(row => {
        console.log(row.join(' '));
    });
}

mask(3);
// 3 3 3
// 3 3 3
// 3 3 3

console.log('-------------------------------------');

mask(7);
// 7 7 7 7 7 7 7
// 7 7 7 7 7 7 7
// 7 7 7 7 7 7 7
// 7 7 7 7 7 7 7
