function mask (params) {
    // MASK

    let amazing = params
        .toString()
        .split('')
        .map(Number)
        .reduce((a, b) => a + b, 0)
        .toString()
        .split('')
        .includes('9');

    amazing ? amazing = 'True' : amazing = "False";

    console.log(`${params} Amazing? ${amazing}`);
}

mask(1233);
// 1233 Amazing? True

mask(999);
// 999 Amazing? False
