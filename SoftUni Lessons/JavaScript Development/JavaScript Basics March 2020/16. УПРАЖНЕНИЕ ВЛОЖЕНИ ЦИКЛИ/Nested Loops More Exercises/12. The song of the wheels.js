function theSongOfTheWheels(input) {
    // Mask
    let m = Number(input.shift());

    let magic = undefined;
    let count = 0;

    let result = '';

    for (let a = 1; a <= 9; a += 1) {
        for (let b = 1; b <= 9; b += 1) {
            for (let c = 1; c <= 9; c += 1) {
                for (let d = 1; d <= 9; d += 1) {
                    if (a < b && c > d) {
                        if ((a * b) + (c * d) == m) {
                            result += `${a}${b}${c}${d} `;
                            count += 1;
                            if (count == 4) {
                                magic = `${a}${b}${c}${d}`;
                            }
                        }
                    } 
                }
            }
        }
    }

    if (result) {
        console.log(result);
    }

    if (count >= 4) {
        console.log(`Password: ${magic}`)
    } else {
        console.log('No!')
    }
    
}

theSongOfTheWheels([11]);  // Should return:
// 1291 1342 1381 1471 1532 1561 1651 1741 1831 1921 2351 2431
// Password: 1471

theSongOfTheWheels([139]);  // Should return:
// No!