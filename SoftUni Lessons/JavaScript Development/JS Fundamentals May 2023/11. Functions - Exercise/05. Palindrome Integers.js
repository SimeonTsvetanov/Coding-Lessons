function mask (nums) {
    // MASK
    nums.forEach(num => {
        (String(num) === String(num).split("").reverse().join("")) ? console.log(true) : console.log(false);
    });
}

mask([123,323,421,121]);
// false
// true
// false
// true

console.log('---------------------------------------');

mask([32,2,232,1010]);
// false
// true
// true
// false
