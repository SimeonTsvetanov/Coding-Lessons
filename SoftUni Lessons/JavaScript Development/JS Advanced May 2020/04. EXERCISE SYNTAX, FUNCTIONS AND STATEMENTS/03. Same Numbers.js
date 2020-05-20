function sameNumbers(num) {
    // Mask
    console.log(new Set(String(num).split('')).size === 1);    
    console.log(String(num).split('').map(Number).reduce((a, b) => a + b, 0));
}

sameNumbers(2222222);  // Should return:
// true
// 14

sameNumbers(1234);  // Should return:
// false
// 10