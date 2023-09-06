function mask (...params) {
    // MASK
    const [a, b, c] = params;
    console.log(Math.max(a, b, c));
}

mask(-2,
7,
3);
// 7

mask(130,
5,
99);
// 130
