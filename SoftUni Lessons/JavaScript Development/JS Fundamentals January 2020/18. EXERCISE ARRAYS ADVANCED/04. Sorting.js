function sorting(array) {
    // Mask
    array.sort((a, b) => a - b)  // Sort the numbers from smallest to biggest.

    let result = [];

    let counter = 0;
    while (array.length > 0) {
        // if counter % 2 == 1: IT will sort by smallest first!
        counter % 2 === 0 ? result.push(array.pop()) : result.push(array.shift());
        counter += 1;
    }

    console.log(...result);
}

sorting([1, 21, 3, 52, 69, 63, 31, 2, 18, 94]);
// Should return: 94 1 69 2 63 3 52 18 31 21
