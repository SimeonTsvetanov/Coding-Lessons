function specialNumbers(times) {
    // Mask
    for (let num = 1; num <= times; num++) {
        let total = 0;
        for (let digit of String(num)) {
            total += Number(digit);
        }
        let special = [5, 7, 11].includes(total) ? 'True' : 'False';

        console.log(`${num} -> ${special}`);
    }
}

specialNumbers(15);  // Should return:
// 1 -> False
// 2 -> False
// 3 -> False
// 4 -> False
// 5 -> True
// 6 -> False
// 7 -> True
// 8 -> False
// 9 -> False
// 10 -> False
// 11 -> False
// 12 -> False
// 13 -> False
// 14 -> True
// 15 -> False
