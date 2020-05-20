"use strict";

function circleArea(radius) {
    // Mask
    if (typeof(radius) === 'number') {
        console.log((Math.PI * radius * radius).toFixed(2));
    } else {
        console.log(`We can not calculate the circle area, because we receive a ${typeof(radius)}.`);
    }
}

circleArea(5);  // Should return: 78.54

circleArea('name');  // Should return:
// We can not calculate the circle area, because we receive a string.