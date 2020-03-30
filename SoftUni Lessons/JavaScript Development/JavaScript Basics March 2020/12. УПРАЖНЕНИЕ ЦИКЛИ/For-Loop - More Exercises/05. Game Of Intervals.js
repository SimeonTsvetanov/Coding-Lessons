function gameOfIntervals(input) {
    // Mask
    let times = Number(input.shift());

    let g1 = 0;
    let g2 = 0;
    let g3 = 0;
    let g4 = 0;
    let g5 = 0;
    let invalid = 0;

    let total = 0;

    for (let i = 1; i <= times; i++) {
        let num = Number(input.shift());
        if (num >= 0 && num <= 9) {
            total += num * 0.2;
            g1 += 1;
        } else if (num >= 10 && num <= 19) {
            total += num * 0.3;
            g2 += 1;
        } else if (num >= 20 && num <= 29) {
            total += num * 0.4;
            g3 += 1;
        } else if (num >= 30 && num <= 39) {
            total += 50;
            g4 += 1;
        } else if (num >= 40 && num <= 50) {
            total += 100;
            g5 += 1;
        } else {
            total = total / 2;
            invalid += 1;
        }
    }

    console.log(`${total.toFixed(2)}`)
    console.log(`From 0 to 9: ${(g1 / times * 100).toFixed(2)}%`)
    console.log(`From 10 to 19: ${(g2 / times * 100).toFixed(2)}%`)
    console.log(`From 20 to 29: ${(g3 / times * 100).toFixed(2)}%`)
    console.log(`From 30 to 39: ${(g4 / times * 100).toFixed(2)}%`)
    console.log(`From 40 to 50: ${(g5 / times * 100).toFixed(2)}%`)
    console.log(`Invalid numbers: ${(invalid / times * 100).toFixed(2)}%`)
}

gameOfIntervals([10, 43, 57, -12, 23, 12, 0, 50, 40, 30, 20]);  // Should return:
// 295.80
// From 0 to 9: 10.00%
// From 10 to 19: 10.00%
// From 20 to 29: 20.00%
// From 30 to 39: 10.00%
// From 40 to 50: 30.00%
// Invalid numbers: 20.00%
