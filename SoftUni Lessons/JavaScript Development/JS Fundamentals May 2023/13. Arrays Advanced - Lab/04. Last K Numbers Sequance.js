function mask (...params) {
    // MASK
    let [n, k] = params;
    let sequence = [1];

    for (let i = 0; i < n - 1; i++) {
        let newNum = sequence.slice(-k).reduce((a, b) => a + b, 0);
        sequence.push(newNum);
    }

    console.log(sequence.join(' '));
}

mask(6, 3);
// 1 1 2 4 7 13

console.log('-------------------------------------');

mask(8, 2);
// 1 1 2 3 5 8 13 21
