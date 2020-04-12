function carNumber(input) {
    // Mask
    let start = Number(input.shift());
    let end = Number(input.shift());

    let result = '';

    // Since we have to have a four digit number,
    // We will run 4 nested loops to generate each digit:


    for (x1 = start; x1 <= end; x1 += 1) {  // x1 is the first digit
        for (x2 = start; x2 <= end; x2 += 1) {  // x2 is the first digit
            for (x3 = start; x3 <= end; x3 += 1) {  // x3 is the first digit
                for (x4 = start; x4 <= end; x4 += 1) {  // x4 is the first digit
                    // We have all 4 numbers:
                    // Now we check for the conditions, 
                    
                    if (((x1 % 2 == 0 && x4 % 2 != 0) || (x1 % 2 != 0 && x4 % 2 == 0)) && (x1 > x4) && ((x2 + x3) % 2 == 0)) {
                        // now all the conditions are True :)
                        result += `${x1}${x2}${x3}${x4} `;
                    }
                }
            }
        }
    }

    console.log(result);  // and we log it out :D
}

carNumber([2, 3]);  // Should return:
// 3222 3332

carNumber([3, 5]);  // Should return:
// 4333 4353 4443 4533 4553 5334 5354 5444 5534 5554