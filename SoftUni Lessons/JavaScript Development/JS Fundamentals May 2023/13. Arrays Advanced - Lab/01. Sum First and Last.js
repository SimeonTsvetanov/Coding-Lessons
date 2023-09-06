function mask (params) {
    // MASK
    nums = params.map(Number)
    console.log(nums[0] + nums[params.length -1]);
}

mask(['20', '30', '40']);
// 60

console.log('-------------------------------------');

mask(['5', '10'] );
// 15
