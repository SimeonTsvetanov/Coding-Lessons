function lotaryStatistics(...input) {
    // Mask
    let number = Number(input.shift()); 
    
    let oddOneNums = 0;
    let evenNums = 0;
    let oddEndingSevenNums = 0;
    let decvidedOnHundred = 0;

    for (let num = 1; num <= number; num++) {
        if (num % 2 != 0 && num < 10) {
            oddOneNums += 1;
        }
        if (num % 2 == 0) {
            evenNums += 1;
        }
        if (num % 2 != 0 && num % 10 == 7) {
            oddEndingSevenNums += 1
        }
        if (100 % num == 0) {
            decvidedOnHundred += 1;
        }
    }

        console.log(`${(oddOneNums / number * 100).toFixed(2)}%`);
        console.log(`${(evenNums / number * 100).toFixed(2)}%`);
        console.log(`${(oddEndingSevenNums / number * 100).toFixed(2)}%`);
        console.log(`${(decvidedOnHundred / number * 100).toFixed(2)}%`);
}

lotaryStatistics(49);  // Should return:
// 10.20%
// 48.98%
// 10.20%
// 14.29%

lotaryStatistics(35);  // Should return:
// 14.29%
// 48.57%
// 8.57%
// 20.00%
