function condense (nums) {
    // MasK
    while(nums.length !== 1) {
        let newNums = []
        nums.forEach((num, idx) => {
            if (idx + 1 < nums.length) {
                newNums.push(nums[idx] + nums[idx + 1]);
            }
        })
        nums = newNums;
    }
    console.log(nums[0]);
}

condense([2,10,3]);
condense([5,0,4,1,2]);
condense([1]);