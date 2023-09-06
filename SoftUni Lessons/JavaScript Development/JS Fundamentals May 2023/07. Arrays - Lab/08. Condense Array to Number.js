function condenseArrayToNumbers(numbersInput) {
    // Mask
    let numbers = numbersInput;
    let condensed = [];

    while (numbers.length > 1) {
        for (let i = 0; i < numbers.length - 1; i += 1) {
            condensed.push(numbers[i] + numbers[i + 1]);
        }
        numbers = condensed;
        condensed = [];
    }
    console.log(numbers[0]);
}

condenseArrayToNumbers([2,10,3]);  // Should return: 25

condenseArrayToNumbers([5,0,4,1,2]);  // Should return: 35