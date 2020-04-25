function NegativePositiveNumbers(array) {
    // Mask
    let result = [];

    for (let num of array) {
        // if num negative it will go at the beginning else it will go to the end of the result.
        num < 0 ? result.unshift(num) : result.push(num);
    }

    result.map(x => console.log(x));
    // console.log(result.join('\n'));  // --> Just Another way f printing the result.
}

NegativePositiveNumbers([7, -2, 8, 9]);  // Should return:
// -2
// 7
// 8
// 9

NegativePositiveNumbers([3, -2, 0, -1]);  // Should return:
// -1
// -2
// 3
// 0
