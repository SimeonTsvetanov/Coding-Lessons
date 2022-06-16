function sumEvenNumbers (numbers) {
    // MasK
    const sumEven = numbers
        .map(Number)
        .filter(function (number) { return number % 2 === 0; })
        .reduce(function (a, b) { return a + b; }, 0);
    console.log(sumEven);
}

sumEvenNumbers(['1','2','3','4','5','6']);