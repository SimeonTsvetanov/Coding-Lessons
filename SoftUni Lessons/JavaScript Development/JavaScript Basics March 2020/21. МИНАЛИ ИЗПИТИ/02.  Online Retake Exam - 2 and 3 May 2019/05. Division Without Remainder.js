function devisionWithoutreminder(input) {
    // Mask
    let total = Number(input.shift());

    let two = 0;
    let three = 0;
    let four = 0;

    for (i = 1; i <= total; i += 1) {
        num = Number(input.shift());
        if (num % 2 == 0) {
            two += 1;
        }
        if (num % 3 == 0) {
            three += 1;
        }
        if (num % 4 == 0) {
            four += 1;
        }
    }

    console.log(`${(two / total * 100).toFixed(2)}%`);
    console.log(`${(three / total * 100).toFixed(2)}%`);
    console.log(`${(four / total * 100).toFixed(2)}%`);
}

devisionWithoutreminder([10, 680, 2, 600, 200, 800, 799, 199, 46, 128, 65,]);  // Should return:
// 70.00%
// 10.00%
// 50.00%

devisionWithoutreminder([3, 3, 6, 9]);  // Should return:
// 33.33%
// 100.00%
// 0.00%
