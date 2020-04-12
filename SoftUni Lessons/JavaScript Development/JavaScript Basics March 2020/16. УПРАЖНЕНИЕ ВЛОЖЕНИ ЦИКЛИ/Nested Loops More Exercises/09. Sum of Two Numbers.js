function sumOfTwoNumbers(input) {
    // Mask
    let start = Number(input.shift());
    let end = Number(input.shift());
    let magic = Number(input.shift());

    let noLuck = true;
    let combinations = 0;

    for (let numOne = start; numOne <= end; numOne += 1) {
        if (!noLuck) {break;}
        for (let numTwo = start; numTwo <= end; numTwo += 1) {
            if (!noLuck) {break;}
            combinations += 1;
            if (numOne + numTwo == magic) {
                console.log(`Combination N:${combinations} (${numOne} + ${numTwo} = ${magic})`);
                noLuck = false;
            }
        }
    }

    if (noLuck) {
        console.log(`${combinations} combinations - neither equals ${magic}`);
    }
}

sumOfTwoNumbers([1, 10, 5]);  // Should return:
// Combination N:4 (1 + 4 = 5)

sumOfTwoNumbers([23, 24, 20]);  // Should return:
// 4 combinations - neither equals 20