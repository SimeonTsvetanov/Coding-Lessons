function evenAndOddSubtraction(array) {
// Mask
    let sumEvens = 0;
    let sumOdds = 0;

    for (let arrayElement of array) {
        Number(arrayElement) % 2 === 0 ? sumEvens += Number(arrayElement) : sumOdds += Number(arrayElement);
    }

    console.log(sumEvens - sumOdds);
}