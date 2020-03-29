function maxNumber(params) {
    // It's stupid to use While here, It should be done with a for loop.

    let times = Number(params.shift());
    let counter = 1;

    let maxNumber = Number.MIN_SAFE_INTEGER;

    while (counter <= times) {
        number = Number(params.shift());
        if (number >= maxNumber) {
            maxNumber = number;
        }

        counter += 1;
    }

    console.log(maxNumber);
}

maxNumber([2, 100, 99]);  // Expected Output:
// 100
