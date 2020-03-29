function sumNumbers(params) {
    let sum = 0;

    let number = params.shift();
    while (number != 'Stop') {
        sum += Number(number);
        number = params.shift();
    }

    console.log(sum);
}


sumNumbers([10, 20, 30, 45, 'Stop']);  // Expected Output: 105
sumNumbers([1, 2, 3, 4, 5, 6, 'Stop']);  // Expected Output: 21