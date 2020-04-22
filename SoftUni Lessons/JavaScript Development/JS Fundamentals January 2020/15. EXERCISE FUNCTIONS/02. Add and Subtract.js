function addAndSubtract(one, two , three) {
    // Mask
    const add = (a, b) => a + b;
    const subtract = (a, b) => a - b;

    let result = subtract(add(one, two), three);

    console.log(result);
}

addAndSubtract(23, 6,10);  // Should return: 19

addAndSubtract(1, 17, 30);  // Should return: -12