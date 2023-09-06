function mask (params) {
    // MASK
    let nums = params.map(Number);
    let new_nums = [];

    nums.forEach(num => {
        (num < 0) ? new_nums.unshift(num) : new_nums.push(num)
    });

    console.log(new_nums.join(`\n`));
}


mask(['7', '-2', '8', '9']);
// -2
// 7
// 8
// 9

console.log('-------------------------------------');

mask(['3', '-2', '0', '-1']);
// -1
// -2
// 3
// 0
