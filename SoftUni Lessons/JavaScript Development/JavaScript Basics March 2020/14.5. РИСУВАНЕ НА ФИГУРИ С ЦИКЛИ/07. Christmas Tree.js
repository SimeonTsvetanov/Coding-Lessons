function christmasTree(input) {
    // Mask
    let n = Number(input.shift());
    for (let row = 0; row <= n; row += 1) {
        console.log(' '.repeat(n - row) + '*'.repeat(row) + ' | ' + '*'.repeat(row) + ' '.repeat(n - row));
    }
}

christmasTree([3]);  // Should return:
//     |
//   * | *
//  ** | **
// *** | ***

christmasTree([4]);  // Should return:
//      |
//    * | *
//   ** | **
//  *** | ***
// **** | ****
