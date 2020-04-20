function maxSequenceOfEqualElements(array) {
    // Mask - FYI - Ugly task
    let max = [];

    let current = [];
    let last = undefined;
    for (let num of array) {
        if (num === last) {
            current.push(num);
        } else {
            current = [];
            current.push(num);
        }
        if (current.length > max.length) {
            max = current;
        }
        last = num;
    }

    console.log(max.join(' '));
}

maxSequenceOfEqualElements([2, 1, 1, 2, 3, 3, 2, 2, 2, 1]);  // Should return: 2 2 2

maxSequenceOfEqualElements([0, 1, 1, 5, 2, 2, 6, 3, 3]);  // Should return: 1 1
