"use strict";

function mathOperations(numOne, numTwo, operator) {
    // Mask
    console.log(eval(`${numOne} ${operator} ${numTwo}`));
}

mathOperations(5, 6, '+');  // Should return: 11

mathOperations(3, 5.5, '*');  // Should return: 16.5