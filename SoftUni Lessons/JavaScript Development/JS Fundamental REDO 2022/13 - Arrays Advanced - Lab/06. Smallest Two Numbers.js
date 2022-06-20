function smallestTwoNumbers (nums) {
    // MasK
    let result = nums.sort((a, b) => a - b, 0).slice(0, 2);
    console.log(result.join(' '));
}

smallestTwoNumbers([30, 15, 50, 5]);