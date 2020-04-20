function addOrSubtract(array) {
    // Mask
    let sumArray = 0;
    let sumModified = 0;

    for (let index = 0; index < array.length; index += 1) {
        let number = Number(array[index]);  // Get the number
        sumArray += number;  // Fill the original number
        // Then modify:
        if (number % 2 === 0) {number += index;}
        else {number -= index;}
        sumModified += number;  // Fill the modified number
        array[index] = number;  // Change the number in the array
    }

    console.log(array);
    console.log(sumArray);
    console.log(sumModified);
}

addOrSubtract([5, 15, 23, 56, 35]);  // Should return:
// [ 5, 14, 21, 59, 31 ]
// 134
// 130

addOrSubtract([-5, 11, 3, 0, 2]);  // Should return:
// [ -5, 10, 1, 3, 6 ]
// 11
// 15
