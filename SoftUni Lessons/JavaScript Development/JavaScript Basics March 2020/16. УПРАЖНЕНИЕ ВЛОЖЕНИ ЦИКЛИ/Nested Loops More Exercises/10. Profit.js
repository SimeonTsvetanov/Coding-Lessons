function profit(input) {
    // Mask
    let maxOne = Number(input.shift());
    let maxTwo = Number(input.shift());
    let maxFive = Number(input.shift());
    let sum = Number(input.shift());

    for (let one = 0; one <= maxOne; one += 1) {
        for (let two = 0; two <= maxTwo; two += 1) {
            for (let five = 0; five <= maxFive; five += 1) {
                if ((one * 1) + (two * 2) + (five * 5) == sum) {
                    console.log(`${one} * 1 lv. + ${two} * 2 lv. + ${five} * 5 lv. = ${sum} lv.`);
                }
            }
        }
    }
}

profit([3, 2, 3, 10]);  // Should return:
// 0 * 1 lv. + 0 * 2 lv. + 2 * 5 lv. = 10 lv.
// 1 * 1 lv. + 2 * 2 lv. + 1 * 5 lv. = 10 lv.
// 3 * 1 lv. + 1 * 2 lv. + 1 * 5 lv. = 10 lv.


profit([5, 3, 1, 7]);  // Should return:
// 0 * 1 lv. + 1 * 2 lv. + 1 * 5 lv. = 7 lv.
// 1 * 1 lv. + 3 * 2 lv. + 0 * 5 lv. = 7 lv.
// 2 * 1 lv. + 0 * 2 lv. + 1 * 5 lv. = 7 lv.
// 3 * 1 lv. + 2 * 2 lv. + 0 * 5 lv. = 7 lv.
// 5 * 1 lv. + 1 * 2 lv. + 0 * 5 lv. = 7 lv.
