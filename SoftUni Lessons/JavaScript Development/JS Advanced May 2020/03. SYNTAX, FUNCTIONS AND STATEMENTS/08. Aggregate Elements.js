function aggregateElements(input) {
    // Mask
    console.log(input.reduce((a,b) => a + b, 0));
    console.log(input.reduce((a,b) => (a) + (1 / b), 0));
    console.log(input.join(''));    
}

aggregateElements([1, 2, 3]);  // Should return:
// 6
// 1.8333
// 123

aggregateElements([2, 4, 8, 16]);  // Should return:
// 30
// 0.9375
// 24816
