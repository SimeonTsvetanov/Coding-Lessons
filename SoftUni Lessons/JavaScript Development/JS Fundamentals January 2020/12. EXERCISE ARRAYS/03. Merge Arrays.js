function mergeArrays(first = [], second = []) {
    // Mask

    /*
    // This is the first option:
    let third = [];
    for (let index = 0; index < first.length; index += 1) {
        if (index % 2 === 0) {
            third.push(Number(first[index]) + Number(second[index]));
        } else {
            third.push(first[index] + second[index]);
        }
    }
    console.log(third.join(' - '));
     */

    // And this is the second option:
    let third = [];
    first.map((element, index) => {
        index % 2 === 0 ?
            third.push(Number(element) + Number(second[index])) :
            third.push(element + second[index]);
    });
    console.log(third.join(' - '));
}

mergeArrays(['5', '15', '23', '56', '35'], ['17', '22', '87', '36', '11']);
// Should return:
// 22 - 1522 - 110 - 5636 - 46

mergeArrays(['13', '12312', '5', '77', '4'], ['22', '333', '5', '122', '44']);
// Should return:
// 35 - 12312333 - 10 - 77122 - 48
