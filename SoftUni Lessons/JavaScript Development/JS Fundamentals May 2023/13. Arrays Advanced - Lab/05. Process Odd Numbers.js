function mask (params) {
    // MASK
    let nums = [];
    params.forEach((num, index) => {
        (index % 2 !== 0) ? nums.push(num * 2) : 'pass';
    });

    console.log(nums.reverse().join(' '));
}

mask([10, 15, 20, 25]);
// 50 30

console.log('-------------------------------------');

mask([3, 0, 10, 4, 7, 3]);
// 6 8 0
