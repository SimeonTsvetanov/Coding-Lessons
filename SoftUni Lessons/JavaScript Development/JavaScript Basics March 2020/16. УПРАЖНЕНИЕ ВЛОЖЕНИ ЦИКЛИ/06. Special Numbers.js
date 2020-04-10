function specialNumbers(input) {
    // Mask
    let n = Number(input.shift());

    result = '';

    for (let i = 1111; i <= 9999; i++) {
        let num = String(i);
        
        let num1 = Number(num[0]);
        let num2 = Number(num[1]);
        let num3 = Number(num[2]);
        let num4 = Number(num[3]);

        if (num1 == 0 || num2 == 0 || num3 == 0 || num4 == 0) {
            continue;
        }

        if (n % num1 == 0 && n % num2 == 0 && n % num3 == 0 && n % num4 == 0) {
            result += `${i} `;
        }
    }

    console.log(result);
}

specialNumbers([3]);  // Should return:
// 1111 1113 1131 1133 1311 1313 1331 1333 3111 3113 3131 3133 3311 3313 3331 3333

specialNumbers([11]);  // Should return:
// 111