function mask (params) {
    // MASK
    let currentYield = params;
    let days = 0;
    let total = 0;

    while (currentYield >= 100) {
        days += 1;
        total += currentYield - 26;
        currentYield -= 10;
    }

    total -= 26;
    (total < 0) ? total = 0 : 'pass';

    console.log(days)
    console.log(total)
}

mask(111);
// 2
// 134

mask(450);
// 36
// 8938
