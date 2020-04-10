function sumOfTwoNumbers(input) {
    // Mask
    let start = Number(input.shift());
    let end = Number(input.shift());
    let magic = Number(input.shift());

    let combinations = 0;
    let found = false;

    for (let x = start; x <= end; x++) {
        for (let y = start; y <= end; y++) {
            combinations ++;
            if (x + y == magic) {
                found = true;
                console.log(`Combination N:${combinations} (${x} + ${y} = ${x + y})`);
                break;  // This breks the loop
            }
        }
        if (found) {break;}  // And this will tell the upper loop to break
    }

    if (!found) {
        console.log(`${combinations} combinations - neither equals ${magic}`)
    }
}

sumOfTwoNumbers([1, 10, 5]);  // Should return:
// Combination N:4 (1 + 4 = 5)

sumOfTwoNumbers([23, 24, 20]);  // Should return:
// 4 combinations - neither equals 20