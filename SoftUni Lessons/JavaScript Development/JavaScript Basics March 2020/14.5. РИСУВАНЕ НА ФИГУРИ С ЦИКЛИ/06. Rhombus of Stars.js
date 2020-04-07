function rhombusOfStars(input) {
    // Mask
    size = Number(input.shift());
    for (let i = 1; i <= size; i += 1) {
        console.log(' '.repeat(size - i) + "* ".repeat(size - (size - i)));
    }
    for (let i = size - 1; i >= 1; i -= 1) {
        console.log(' '.repeat(size - i) + "* ".repeat(size - (size - i)));
    }
}

rhombusOfStars([4]);  // Should return:
//    *
//   * *
//  * * *
// * * * *
//  * * *
//   * *
//    *

rhombusOfStars([3]);  // Should return:
//   *
//  * *
// * * *
//  * *
//   *
