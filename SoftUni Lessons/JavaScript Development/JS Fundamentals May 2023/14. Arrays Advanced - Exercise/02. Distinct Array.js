function mask (nums) {
    // MASK
    console.log([...new Set(nums)].join(' '))
}

mask([1, 2, 3, 4]);
// 1 2 3 4

console.log('-------------------------------------');

mask([7, 8, 9, 7, 2, 3, 4, 1, 2]);
// 7 8 9 2 3 4 1
