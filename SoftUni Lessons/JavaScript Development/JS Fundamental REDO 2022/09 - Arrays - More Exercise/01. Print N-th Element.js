function printNthElement (array) {
    // MasK
    let n = Number(array.pop());  // Get the last Element:

    let collected = [];  // Collected Nth elements will be stored here!

    // Now lets collect them numbers:
    for (let index = 0; index < array.length; index += n) {
        collected.push(array[index]);
    }

    // And Finally print the result:
    console.log(collected.join(' '));
}

printNthElement(['5', '20', '31', '4', '20', '2']);  // 5 31 20
printNthElement(['dsa', 'asd', 'test', 'test', '2']);  // dsa test
printNthElement(['1', '2', '3', '4', '5', '6'])  // 1