function lastKNumberSequence(n, k) {
    // Mask
    let array = [1];
    for (let index = 0; index < n - 1; index++) {
        let sumArray = array.slice(Math.max(0, index - k + 1), index + 1).reduce((a, b) => a + b, 0);
        array.push(sumArray);
    }
    console.log(array.join(' '));
}

lastKNumberSequence(6, 3);  // Should return: 1 1 2 4 7 13

lastKNumberSequence(8, 2);  // Should return: 1 1 2 3 5 8 13 21
