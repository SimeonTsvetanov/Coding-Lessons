// Not included in final score

function arrayManipulator(array, commands) {
    // Mask
    function add(index, element) {
        // adds element at the specified index
        array.splice(index, 0, element);
    }
    
    function addMany(index, nums) {
        // adds a set of elements at the specified index
        array.splice(index, 0, ...nums);
    }

    function contains(element) {
        // print index of first occurrence else print -1
        array.includes(element) ? console.log(array.indexOf(element)) : console.log(-1);
    }

    function remove(index) {
        // removes the element at the specified index
        array.splice(index, 1);
    }

    function shift(positions) {
        // Shifts to the left
        // For example, [1, 2, 3, 4, 5] -> shift 2 -> [3, 4, 5, 1, 2]
        for (let position = 1; position <= positions; position += 1) {
            array.push(array.shift());
        }
    }

    function sumPairs() {
        // sums the elements in the array by pairs (first + second, third + fourth, …)
        array = array.map((e, i, array) => i < array.length - 1 ? (array[i] += array[i + 1]) : array[i] = array[i]).filter((e, i) => i % 2 === 0);
    }

    while ('command is not print') {
        let data = commands.shift().split(' ');
        let command = data.shift();

        if (command === 'print') {
            console.log(`[ ${array.join(", ")} ]`);
            break;
        } else if (command === 'add') {
            add(Number(data.shift()), Number(data.shift()));
        } else if (command === 'addMany') {
            addMany(Number(data.shift()), data.map(Number));
        } else if (command === 'contains') {
            contains(Number(data.shift()));
        } else if (command === 'remove') {
            remove(Number(data.shift()));
        } else if (command === 'shift') {
            shift(Number(data.shift()));
        } else if (command === 'sumPairs') {
            sumPairs();
        }
    }
}


// arrayManipulator([1, 2, 3, 4, 5], ['shift 2', 'print']);

arrayManipulator([1, 2, 4, 5, 6, 7], ['add 1 8', 'contains 1', 'contains 3', 'print']);
// Should return:
// 0
// -1
//     [ 1, 8, 2, 4, 5, 6, 7 ]

arrayManipulator([1, 2, 3, 4, 5], ['addMany 5 9 8 7 6 5', 'contains 15', 'remove 3', 'shift 1', 'print']);
// Should return:
// -1
// [ 2, 3, 5, 9, 8, 7, 6, 5, 1 ]

