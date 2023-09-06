function mask (a, b) {
    // MASK
    function factorial(n) {
        if (n === 0) return 1;
        return n * factorial(n - 1);
    }

    console.log(`${(factorial(a) / factorial(b)).toFixed(2)}`);
}

mask(5,
2
);
// 60.00

console.log('-------------------------------------');

mask(6,
2
);
// 360.00
