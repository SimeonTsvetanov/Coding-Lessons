function mask (params) {
    // MASK
    let nums = params;

    let max_sequence = [];

    nums.forEach((num, index) => {
        let current_sequence = [num];

        for(let i = index + 1; i < nums.length; i++) {
            if (nums[i] === num) {
                current_sequence.push(nums[i]);
            } else {
                break;
            }
        }

        (current_sequence.length > max_sequence.length) ? max_sequence = current_sequence : 'pass';
    });

    console.log(...max_sequence);
}

mask([2, 1, 1, 2, 3, 3, 2, 2, 2, 1]);
// 2 2 2

mask([1, 1, 1, 2, 3, 1, 3, 3]);
// 1 1 1
