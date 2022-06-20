function oddAndEvenSum (num) {
    // MasK
    function oddSum(num) {
        return num
            .toString()
            .split('')
            .map(Number)
            .filter(n => {return n % 2 !== 0}, 0)
            .reduce((a, b) => a + b, 0);
    }

    function evenSum(num) {
        return num
            .toString()
            .split('')
            .map(Number)
            .filter(n => {return n % 2 === 0}, 0)
            .reduce((a, b) => a + b, 0);
    }

    console.log(`Odd sum = ${oddSum(num)}, Even sum = ${evenSum(num)}`);
}

oddAndEvenSum(1000435);  //  Odd sum = 9, Even sum = 4