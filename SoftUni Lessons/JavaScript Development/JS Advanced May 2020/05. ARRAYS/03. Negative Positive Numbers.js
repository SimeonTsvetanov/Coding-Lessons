function negarivePositioveNumbers(array = []) {
    // Mask
    let sorted = [];
    
    array.forEach(element => {
        element < 0 ? sorted.unshift(element) : sorted.push(element);
    });

    console.log(sorted.join('\n'));
}

negarivePositioveNumbers([7, -2, 8, 9]);  // Should return:
// -2
// 7
// 8
// 9

negarivePositioveNumbers([3, -2, 0, -1]);  // Should return:
// -1
// -2
// 3
// 0
