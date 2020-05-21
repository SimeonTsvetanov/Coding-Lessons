'use strict';
function firstLast(array = []) {
    // Mask
    console.log(Number(array[0]) + Number(array[array.length - 1]));
}

firstLast(['20', '30', '40']);  // Should return: 60

firstLast(['5', '10']);  // Should return: 15
