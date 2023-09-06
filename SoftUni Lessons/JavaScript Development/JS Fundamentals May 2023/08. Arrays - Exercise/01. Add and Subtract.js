function mask (params) {
    // MASK
    let original_nums = params;
    let modified_nums = [];

    original_nums.forEach((num, index) => {
        (num % 2 === 0)
            ? modified_nums.push(num + index)
            : modified_nums.push(num - index);
    })

    let sum_original_nums = original_nums.reduce((a, b) => a + b, 0);
    let sum_modified_nums = modified_nums.reduce((a, b) => a + b, 0);

    console.log(modified_nums);
    console.log(sum_original_nums);
    console.log(sum_modified_nums);
}

mask([5, 15, 23, 56, 35]);
// [ 5, 14, 21, 59, 31 ]
// 134
// 130

mask([-5, 11, 3, 0, 2]);
// [ -5, 10, 1, 3, 6 ]
// 11
// 15
