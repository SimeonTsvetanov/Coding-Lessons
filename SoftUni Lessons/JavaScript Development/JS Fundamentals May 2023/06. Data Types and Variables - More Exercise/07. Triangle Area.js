function mask (...params) {
    // MASK
    const [a, b, c] = params;
    const s = (a + b + c) / 2;
    const area = Math.sqrt(s * ((s - a) * (s - b) * (s - c)));
    console.log(area);
}

mask(2,
3.5,
4);
// 3. 4994419197923547

mask(3,
5.5,
4);
// 5.854685623498498
