function magicSum(array, magic) {
    // Mask
    for (let num = 0; num < array.length; num += 1) {
        for (let next = num + 1; next < array.length; next += 1) {
            if (array[num] + array[next] === magic) {
                console.log(`${array[num]} ${array[next]}`);
            }
        }
    }
}

magicSum([1, 7, 6, 2, 19, 23], 8);  // Should return:
// 1 7
// 6 2

magicSum([14, 20, 60, 13, 7, 19, 8], 27);  // Should return:
// 14 13
// 20 7
// 19 8

