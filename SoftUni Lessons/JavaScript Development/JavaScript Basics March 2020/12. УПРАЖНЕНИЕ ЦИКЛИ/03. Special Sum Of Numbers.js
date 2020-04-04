function spacialSumOfNumbers(...input) {
    // Mask
    let start = Number(input.shift());
    let end  = Number(input.shift());
    let devider = Number(input.shift());

    let number = start;
    let sum = 0;

    for (number; number <= end; number++) {
        if (number % devider == 0) {
            sum += number
        }
    }

    console.log(sum);
}

spacialSumOfNumbers(10, 30, 7);  // Should return: 63

spacialSumOfNumbers(61, 125, 25);  // Should return: 300
