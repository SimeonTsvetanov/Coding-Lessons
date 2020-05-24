function extractIncreasingSubSequenceFromArray(array) {
    // Mask
    let extracted = [array.shift()]
    array.filter(number => {
        let biggest = Math.max(...extracted);
        number >= biggest ? extracted.push(number) : 'pass';
    })
    console.log(extracted.join('\n'));
}

extractIncreasingSubSequenceFromArray([1, 3, 8, 4, 10, 12, 3, 2, 24]);
// Should return:
// 1
// 3
// 8
// 10
// 12
// 24

extractIncreasingSubSequenceFromArray([20, 3, 2, 15, 6, 1]);
// Should return:
// 20