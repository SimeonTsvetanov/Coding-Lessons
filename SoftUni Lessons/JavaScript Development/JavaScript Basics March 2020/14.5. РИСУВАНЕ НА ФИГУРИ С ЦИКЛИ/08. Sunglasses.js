function sunglasses(input) {
    // Mask
    let n = Number(input.shift());
    console.log('*'.repeat(2 * n) + ' '.repeat(n) + '*'.repeat(2 * n));
    for (let i = 0; i < n - 2; i += 1) {
        let glass = '*' + '/'.repeat(2 * n - 2) + '*';
        if (i == Math.floor((n - 1) / 2 - 1)) { glass += "|".repeat(n); }
        else { glass += ' '.repeat(n); }
        glass += '*' + '/'.repeat(2 * n -2) + '*';
        console.log(glass);
    }
    console.log('*'.repeat(2 * n) + ' '.repeat(n) + '*'.repeat(2 * n));
}

sunglasses([4]);  // Should return:
// ********    ********
// *//////*||||*//////*
// *//////*    *//////*
// ********    ********

sunglasses([3]);  // Should return:
// ******   ******
// *////*|||*////*
// ******   ******
