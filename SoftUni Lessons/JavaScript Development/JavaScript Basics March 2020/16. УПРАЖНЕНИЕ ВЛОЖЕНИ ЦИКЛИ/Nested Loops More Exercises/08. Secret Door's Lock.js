function secretDoorsLock(input) {
    // Mask
    let num3 = Number(input.shift());
    let num2 = Number(input.shift());
    let num1 = Number(input.shift());

    for (let x1 = 1; x1 <= num3; x1 += 1) {
        for (let x2 = 1; x2 <= num2; x2 += 1) {
            for (let x3 = 1; x3 <= num1; x3 += 1) {
                if (x1 % 2 == 0 && x3 % 2 == 0) {
                    if (x2 == 2 || x2 == 3 || x2 == 5 || x2 == 7) {
                        console.log(`${x1} ${x2} ${x3}`);
                    }
                }
            }
        }
    }
}

secretDoorsLock([3, 5, 5]);  // Should return:
// 2 2 2
// 2 2 4
// 2 3 2
// 2 3 4
// 2 5 2
// 2 5 4

secretDoorsLock([8, 2, 8]);  // Should return:
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
