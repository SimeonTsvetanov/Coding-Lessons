function distinctArray(array) {
    // Mask
    let result = [];

    for (let number of array) {
        // If we don't have the number in the result array, we will append it.
        !(result.includes(number)) ? result.push(number) : 'pass';
    }

    console.log(...result);
}

distinctArray([1, 2, 3, 4]);  // Should return: 1 2 3 4

distinctArray([7, 8, 9, 7, 2, 3, 4, 1, 2]);  // Should return: 7 8 9 2 3 4 1