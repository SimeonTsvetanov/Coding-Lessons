function halfSumElement(params) {
    let count = Number(params.shift());

    let restNumbers = 0;
    let maxNumber = Number.MIN_SAFE_INTEGER;

    for (i = 1; i <= count; i++) {
        number = Number(params.shift());
        restNumbers += number;
        if (number >= maxNumber) {maxNumber = number;}
    }
    restNumbers -= maxNumber

    if (restNumbers == maxNumber) {
        console.log(`Yes`);
        console.log(`Sum = ${maxNumber}`);
    } else {
        console.log(`No`);
        console.log(`Diff = ${Math.abs(maxNumber - restNumbers)}`)
    }
}

halfSumElement([7, 3, 4, 1, 1, 2, 12, 1]);  // Expected Output:
// Yes
// Sum = 12

halfSumElement([4, 6, 1, 2, 3]);  // Expected Output:
// Yes
// Sum = 6

halfSumElement([3, 1, 1, 10]);  // Expected Output:
// No
// Diff = 8


