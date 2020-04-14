function triangleOfNumbers(stop) {
    // Mask
    
    // for (let row = 1; row <= stop; row += 1) {
    //     let result = '';
    //     for (let col = 1; col <= row; col += 1) {
    //         result += `${row} `;
    //     }
    //     console.log(result);
    // }

    for (let i = 1; i <= stop; i++) {
        console.log(`${i} `.repeat(i));
    }
}

triangleOfNumbers(3);  // Should return:
// 1
// 2 2 
// 3 3 3

triangleOfNumbers(5);  // Should return:
// 1
// 2 2 
// 3 3 3
// 4 4 4 4
// 5 5 5 5 5
