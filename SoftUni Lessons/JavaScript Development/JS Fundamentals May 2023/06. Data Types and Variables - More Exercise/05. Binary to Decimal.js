function mask (params) {
    // MASK
    const binary = params;
    const decimal = parseInt(binary, 2);
    console.log(decimal);
}

mask(000001001);
// 9

mask(11110000);
// 240
