function maxNumbers(array) {
    // Mask
    /*
    // First way to solve the task.
    let top = [];

    for (let index = 0; index <= array.length; index += 1) {
        let number = array[index];

        let isTop = true;
        for (let next = index + 1; next <= array.length; next += 1) {
            let nextNumber = array[next];
            if (nextNumber >= number) {
                isTop = false;
            }
        }
        if (isTop) {
            top.push(number);
        }
    }

    console.log(top.join(' '));
    */

    // Second way to solve the task:
    let top = []
    array.map((number, index) => {
        let right = array.slice(index + 1, array.length);
        let all = true
        right.map((nextNumber, nextIndex) => {
            nextNumber >= number ? all = false : 'pass';
        });
        all ? top.push(number) : 'pass';
    });
    console.log(top.join(' '));
}

maxNumbers([1, 4, 3, 2]);  // Should return: 4 3 2

maxNumbers([14, 24, 3, 19, 15, 17]);  // Should return: 24 19 17
