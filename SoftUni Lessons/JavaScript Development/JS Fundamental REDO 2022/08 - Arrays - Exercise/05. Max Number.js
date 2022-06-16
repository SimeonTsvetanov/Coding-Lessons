function maxNumbers (nums) {
    // MasK
    let topIntegers = [];

    nums.forEach((num, index) => {
        let rest = nums.slice(index + 1, nums.length);
        if (rest.every(n => n < num)) {
            topIntegers.push(num);
        }
    });

    console.log(topIntegers.join(' '));
}

maxNumbers([1, 4, 3, 2]);
maxNumbers([14, 24, 3, 19, 15, 17]);
maxNumbers([41, 41, 34, 20]);