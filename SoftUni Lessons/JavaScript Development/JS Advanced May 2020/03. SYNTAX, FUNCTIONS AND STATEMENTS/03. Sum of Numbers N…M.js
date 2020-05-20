"use strict";

function sumOfNumbersNtoM(n, m) {
    // Mask
    let sum = 0;
    for (let i = Number(n); i <= Number(m); i++) {
        sum += i;
    }
    console.log(sum);
}

sumOfNumbersNtoM('1', '5');  // Should return: 15

sumOfNumbersNtoM('-8', '20');  // Should return: 174