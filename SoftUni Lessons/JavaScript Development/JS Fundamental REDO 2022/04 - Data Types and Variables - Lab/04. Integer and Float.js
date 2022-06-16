function integersAndFloats(a, b, c) {
    n = a + b + c;
    if (Number(n) === n && n % 1 !== 0) {
        console.log(`${n} - Float`);
    } else {
        console.log(`${n} - Integer`);
    }
}