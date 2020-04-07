function house(input) {
    // Mask
    let n = Number(input.shift());
    let stars = 1;
    if (n % 2 == 0) { stars += 1; };
    for (let i = 0; i < (n + 1) / 2; i += 1) {
        let dash = Math.ceil((n - stars) / 2);
        if (dash < 0) { break; }
        console.log('-'.repeat(dash) + '*'.repeat(stars) + '-'.repeat(dash));
        stars+=2;
    }
    for (let j = 1; j <= n / 2; j += 1) {
        console.log('|' + '*'.repeat(n -2) + '|');
    }
}

house([2]);  // Should return:
// **
// ||

house([5]);  // Should return:
// --*--
// -***-
// *****
// |***|
// |***|
