function equalSums(array) {
    // Mask
    /*
    // The common way of solving the task:
    let notLucky = true;

    for (let index = 0; index < array.length; index += 1) {
        let left = 0;
        let right = 0;

        // fill the left:
        for (let lIndex = 0; lIndex < index; lIndex += 1) {left += array[lIndex];}
        // fill the right:
        for (let rIndex = index + 1; rIndex < array.length; rIndex += 1) {right += array[rIndex];}
        // check for luck:
        if (left === right) {
            console.log(index);
            notLucky = false;
            break;
        }
    }

    if (notLucky) {console.log('no');}
    */

    // And the advanced way of solving it:
    let noLuck = true;
    array.map((num, index) => {
        let right = (array.slice(index + 1, array.length)).reduce((a, b) => a + b, 0);
        let left = (array.slice(0, index)).reduce((a, b) => a + b, 0);
        if (left === right && noLuck) {console.log(index); noLuck = false;}
    });
    noLuck ? console.log('no') : 'pass';
}

equalSums([1, 2, 3, 3]);  // Should return: 2

equalSums([1, 2]);  // Should return: 'no'

