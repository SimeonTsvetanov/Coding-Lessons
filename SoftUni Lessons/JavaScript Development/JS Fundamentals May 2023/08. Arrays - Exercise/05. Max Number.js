function mask (params) {
    // MASK
    let nums = params;
    let top_integers = []

    nums.forEach((num, index) => {
        let valid = true;
        for(let i = index + 1; i < nums.length; i++) {
            (num <= nums[i]) ? valid = false : 'pass';
        }
        (valid) ? top_integers.push(num) : 'pass';
    });

    console.log(...top_integers);
}

mask([1, 4, 3, 2]);
// 4 3 2

mask([14, 24, 3, 19, 15, 17]);
// 24 19 17
