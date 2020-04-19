function evenAndOddSubtraction(array) {
// Mask
    let sumEvens = 0;
    let sumOdds = 0;

    for (let arrayElement of array) {
        Number(arrayElement) % 2 === 0 ? sumEvens += Number(arrayElement) : sumOdds += Number(arrayElement);
    }

    console.log(sumEvens - sumOdds);
}

evenAndOddSubtraction([1,2,3,4,5,6]);  // Should return: 3

evenAndOddSubtraction([3,5,7,9]);  // Should return: -24