function minNumber(params) {
    // It's stupid to use While here, It should be done with a for loop.
    // yeah, yeah same as last taks...

    let times = Number(params.shift());
    let counter = 1;

    let minNumber = Number.MAX_SAFE_INTEGER;

    while (counter <= times) {
        number = Number(params.shift());
        if (number <= minNumber) {
            minNumber = number;
        }

        counter += 1;
    }

    console.log(minNumber);
}


minNumber([2, 100, 99]);  // Expected Output:
// 99
