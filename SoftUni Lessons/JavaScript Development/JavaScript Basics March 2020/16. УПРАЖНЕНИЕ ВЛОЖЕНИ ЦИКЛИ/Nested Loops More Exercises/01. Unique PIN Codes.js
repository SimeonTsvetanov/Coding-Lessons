function uniquePinCodes(input) {
    // Mask
    let n1 = Number(input.shift());
    let n2 = Number(input.shift());
    let n3 = Number(input.shift());

    for (x1 = 1; x1 <= n1; x1 += 1) {
        for (x2 = 1; x2 <= n2; x2 += 1) {
            for (x3 = 1; x3 <= n3; x3 += 1) {
                if (x1 % 2 == 0 && [2, 3, 5, 7].includes(x2) && x3 % 2 == 0) {
                    // WE HAVE A MATCH
                    console.log(`${x1} ${x2} ${x3}`);
                }
            }
        }
    }
}

uniquePinCodes([3, 5, 5]);  // Should return:
// 2 2 2
// 2 2 4
// 2 3 2
// 2 3 4
// 2 5 2
// 2 5 4

console.log();  // Just add a empty space for better readability.

uniquePinCodes([8, 2, 8]);  // Should return:
// 2 2 2
// 2 2 4
// 2 2 6
// 2 2 8
// 4 2 2
// 4 2 4
// 4 2 6
// 4 2 8
// 6 2 2
// 6 2 4
// 6 2 6
// 6 2 8
// 8 2 2
// 8 2 4
// 8 2 6
// 8 2 8
