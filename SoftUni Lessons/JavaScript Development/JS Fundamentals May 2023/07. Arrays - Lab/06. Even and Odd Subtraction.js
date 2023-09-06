function mask (nums) {
    // MASK
    const sum_even = nums.filter(x => x % 2 === 0).reduce((a, b) => a + b, 0);
    const sum_odd = nums.filter(x => x % 2 !== 0).reduce((a, b) => a + b, 0);
    console.log(sum_even - sum_odd);
}

mask([1,2,3,4,5,6]);
// 3

mask([3,5,7,9] );
// -24
