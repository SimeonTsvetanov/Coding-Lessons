function mask (...params) {
    // MASK
    const [a, b, c] = params;
    const n = a + b + c;
    (Number(n) === n && n % 1 !== 0) ? console.log(`${n} - Float`) : console.log(`${n} - Integer`);
}

mask(9, 100, 1.1);
// 110.1 - Float

mask(100, 200, 303 );
// 603 - Integer
