"use strict";
function squareOfStarts(num) {
    // Mask
    num ? num : num = 5;
    
    for (let row = 1; row <= num; row ++) {
        console.log('* '.repeat(num));
    }
}

squareOfStarts(2);  // Should return:
// * *
// * *

squareOfStarts();  // Should return:
// * * * * *
// * * * * *
// * * * * *
// * * * * *
// * * * * *
