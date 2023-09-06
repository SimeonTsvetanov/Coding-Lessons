function mask (num) {
    // MASK
    let nums = String(num).split('').map(Number);



    while ('i say so!') {
    if ((nums.reduce((a, b) => a + b, 0) / nums.length) >= 5) {
        return nums.join('');
    } else {
        nums.push(9);
    }

    }
}

console.log(mask(101));
// 1019999

console.log('-------------------------------------');

console.log(mask(5835));
// 5835
