function sumEvenNumbers(array) {
    // Mask
    let sum = 0

    for (let num of array) {
        Number(num) % 2 === 0 ? sum += Number(num) : 'Do Nothing for f**k sake';
    }

    console.log(sum);
}

sumEvenNumbers(['1','2','3','4','5','6']);  // Should return: 12

sumEvenNumbers(['3','5','7','9']);  // Should return: 0