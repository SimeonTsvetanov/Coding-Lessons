function oddAndEvenSum(input) {
    // Mask
    const getSum = (array) => {
        let even = 0; let odd = 0;
        for (let number of array) { number % 2 === 0 ? even += number : odd += number; }
        return [even, odd]
    };

    let sums = getSum(String(input).split('').map(Number));
    console.log(`Odd sum = ${sums[1]}, Even sum = ${sums[0]}`);
}

oddAndEvenSum(1000435);
// Should return: Odd sum = 9, Even sum = 4

oddAndEvenSum(3495892137259234);
// Should return: Odd sum = 54, Even sum = 22