function arrayManipulator(input) {
    // Mask
    let array = input.shift().split(' ').map(Number);

    for (let data of input) {
        let [command, firstNum, secondNum] = data.split(' ');

        command === 'Add' ? array.push(Number(firstNum)) : 'pass';
        command === 'Remove' ?  array = array.filter(x => x !== Number(firstNum)) : 'pass';
        command === 'RemoveAt' ?  array.splice(Number(firstNum), 1) : 'pass';
        command === 'Insert' ? array.splice(Number(secondNum), 0, Number(firstNum)) : 'pass';
    }

    console.log(...array);
}

arrayManipulator(['4 19 2 53 6 43', 'Add 3', 'Remove 2', 'RemoveAt 1', 'Insert 8 3']);  // Should return: 4 53 6 8 43 3
