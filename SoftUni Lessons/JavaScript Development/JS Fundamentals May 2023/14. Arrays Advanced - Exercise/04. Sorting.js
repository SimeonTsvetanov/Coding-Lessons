function sorting (nums) {
    // MasK
    nums.sort((a, b) => b - a);

    let sorted = [];

    while (nums.length >= 1) {
        sorted.push(nums.shift());
        nums.length >= 1 ? sorted.push(nums.pop()) : 'pass';
    }

    console.log(...sorted);
}

sorting([1, 21, 3, 52, 69, 63, 31, 2, 18, 94]);
// 94 1 69 2 63 3 52 18 31 21
