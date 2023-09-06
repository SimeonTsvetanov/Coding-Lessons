function mask (params) {
    // MASK
    let total = params.toString().split('').map(Number).reduce((a, b) => a + b, 0);
    console.log(total);
}

mask(245678);
// 32

mask(97561);
// 28
