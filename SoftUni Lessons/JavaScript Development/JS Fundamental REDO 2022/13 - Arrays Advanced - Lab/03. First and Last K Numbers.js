function firstAndLastKNumbers (numbers) {
    // MasK
    // Write a function that prints the first k and the last k elements from an array of numbers.
    // The input comes as an array of number elements. The first element represents the number k, all other elements are from the array that needs to be processed.
    // The output is printed on the console on two lines. On the first line, print the first k elements, separated by space. On the second line, print the last k elements, separated by space.

    // AI Solution:
    let k = numbers.shift();
    console.log(numbers.slice(0, k).join(' '));
    console.log(numbers.slice(numbers.length - k).join(' '));
}

firstAndLastKNumbers(['2', '7', '8', '9']);
// 7 8
// 8 9

firstAndLastKNumbers([3,
    6, 7, 8, 9]
);
// 6 7 8
// 7 8 9
