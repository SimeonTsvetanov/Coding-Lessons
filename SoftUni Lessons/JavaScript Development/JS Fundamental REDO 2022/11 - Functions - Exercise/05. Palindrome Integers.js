function palindromeIntegers (integers) {
    // MasK
    integers.map(int => int.toString()).forEach(i => {
        console.log(new Set([i, i.split('').reverse().join('')]).size === 1);
    });
}

palindromeIntegers([123,323,421,121]);

// false
// true
// false
// true
