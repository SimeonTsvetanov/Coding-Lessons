function mask (num) {
    // MASK

    let nums = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'};
    let last = Number(num.toString().split('').pop())
    console.log(nums[last])
}

mask(512);
//

mask(1);
//

