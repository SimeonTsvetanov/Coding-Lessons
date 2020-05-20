"use strict";
function largestNumber(numOne, numTwo, numThree) {
    // Mask
    console.log(`The largest number is ${Math.max(...arguments)}.`);
}

largestNumber(5, -3, 16);  // Should return:
// The largest number is 16.

largestNumber(-3, -5, -22.5);  // Should return:
// The largest number is -3.