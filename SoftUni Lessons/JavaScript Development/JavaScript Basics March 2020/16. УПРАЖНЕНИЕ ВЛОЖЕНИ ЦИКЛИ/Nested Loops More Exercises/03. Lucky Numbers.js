function luckyBasters(input) {
    // Mask
    let result = '';  // Here we keep the result.

    n = Number(input.shift());
    
    // 4-цифрени числа(всяка цифра от числото е в интервала [1...9]). 
    // So... we need 4 loops from one to nine:

    for (x1 = 1; x1 <= 9; x1 += 1) {  // x1 is the first digit
        for (x2 = 1; x2 <= 9; x2 += 1) {  // x2 is the first digit
            for (x3 = 1; x3 <= 9; x3 += 1) {  // x3 is the first digit
                for (x4 = 1; x4 <= 9; x4 += 1) {  // x4 is the first digit
                    // Now we check for the conditions:
                    if (((x1 + x2) == (x3 + x4)) && (n % (x1 + x2) == 0)) {
                        result += `${x1}${x2}${x3}${x4} `;
                    }
                }
            }
        }
    }

    console.log(result) // chao.
}

luckyBasters([3]);  // Should return:
// 1212 1221 2112 2121

luckyBasters([7]);  // Should return:
// 1616 1625 1634 1643 1652 1661 2516 2525 2534 2543 2552 2561 3416 3425 3434 3443 3452 3461 4316 4325 4334 4343 4352 4361 5216 5225 5234 5243 5252 5261 6116 6125 6134 6143 6152 6161