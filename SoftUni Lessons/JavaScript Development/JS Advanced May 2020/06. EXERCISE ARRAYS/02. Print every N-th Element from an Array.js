function printEveryNthElementFromAnArray(array = []) {
    // Mask
    const step = Number(array.pop());
    for (let element = 0; element < array.length; element += step) {
        console.log(array[element]);
    }
}

printEveryNthElementFromAnArray([
    '5',
    '20',
    '31',
    '4',
    '20',
    '2']
);
// Should return:
// 5
// 31
// 20

printEveryNthElementFromAnArray([
    'dsa',
    'asd',
    'test',
    'tset',
    '2']
);
// Should return:
// dsa
// test
