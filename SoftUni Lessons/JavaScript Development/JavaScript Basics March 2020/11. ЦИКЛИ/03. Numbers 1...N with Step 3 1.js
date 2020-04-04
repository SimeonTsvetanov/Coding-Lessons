function oneToNWithStepthree(...params) {
    stop = params.shift();
    for (let number = 1; number <= stop; number += 3) {
        console.log(number);
    }
}

oneToNWithStepthree(10);  // Expected Output: 1/ 4/ 7/ 10/ Each on new line.
