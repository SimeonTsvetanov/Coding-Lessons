function mask (params) {
    // MASK
    console.log(params.sort((a, b) => a - b).slice(0, 2).join(' '));
}

mask([30, 15, 50, 5]);
// 5 15

console.log('-------------------------------------');

mask([3, 0, 10, 4, 7, 3]);
// 0 3
