function mask (...params) {
    // MASK
    let start = params.shift();
    let end = params.shift();

    let nums = [];
    for (let i = start; i <= end; i++) {
        nums.push(i);
    }

    console.log(nums.join(' '));
    console.log(`Sum: ${nums.reduce((a, b) => a + b, 0)}`)
}

mask(5, 10);
// 5 6 7 8 9 10
// Sum: 45

mask(0, 26);
// 0 1 2 … 26
// Sum: 351
