function palindromeIntegers(nums) {
    // Mask
    for (let num of nums.map(String)) {
        console.log(num === num.split('').reverse().join(''));
    }
}

palindromeIntegers([123,323,421,121]);
// Should return:
// false
// true
// false
// true

palindromeIntegers([32,2,232,1010]);
// Should return:
// false
// true
// true
// false
