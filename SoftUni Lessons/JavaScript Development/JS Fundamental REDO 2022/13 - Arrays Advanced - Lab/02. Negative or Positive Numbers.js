function negativeOrPositive (arr) {
    // MasK
    // Write a function that processes the elements in an array one by one and produces a new array.
    // Prepend each negative element at the front of the array
    // (as the first element) and append each positive (or 0) element at the end of the array.
    // The input comes as an array of string elements holding numbers.
    // The output is printed on the console, each element on a new line.

    // Solution
    let result = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] < 0) {
            result.unshift(arr[i]);
        } else {
            result.push(arr[i]);
        }
    }
    console.log(result.join('\n'));
}

negativeOrPositive(['7', '-2', '8', '9']);

// -2
// 7
// 8
// 9
