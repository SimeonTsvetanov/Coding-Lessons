function lastKNumbersSequence(n, k) {
    // Mask  --> This task is ugly
    let result = [1];

    for (let i = 1; i < n; i++) {
        // Start of slice current index(if we start from 1) - k (given number)... but if less then zero IT HAS TO BE ZERO.
        // End of slice is  the current index (as we start from 1 (not from 0).)
        let a = result.slice(Math.max(0, i - k), i);
        let sum = a.reduce((x, y) => x + y, 0);  // Used the reduce method to sum the array.
        result.push(sum);  // Adn fill it in the result
    }

    console.log(...result);  // short hand of printing with space in between.
}

lastKNumbersSequence(6, 3);  // Should return: 1 1 2 4 7 13

lastKNumbersSequence(8, 2);  // Should return: 1 1 2 3 5 8 13 21
