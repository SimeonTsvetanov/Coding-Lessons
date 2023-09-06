function mask (params) {
    // MASK
    let k = params.shift();
    let nums = params;

    let first =  nums.slice(0, k);
    let last = nums.slice(nums.length - k, nums.length);

    console.log(first.join(' '));
    console.log(last.join(' '));
}

mask([2, 7, 8, 9]);
// 7 8
// 8 9

console.log('-------------------------------------');

mask([3, 6, 7, 8, 9]);
// 6 7 8
// 7 8 9
