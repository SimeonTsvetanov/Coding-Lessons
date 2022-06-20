function arrayManipulations (data) {
    // MasK
    let nums = data.shift().split(' ').map(Number);

    let manipulations = {
        'Add': (array, num) => {
            return array.push(+num);
        },
        "Remove": (array, item) => {
            for(let i = 0; i < array.length; i++){
                if(array[i] === +item) {
                    array.splice(array.indexOf(+item), 1);
                    i--;
                }
            }
        },
        'RemoveAt': (array, index) => {
            array.splice(+index, 1);
        },
        'Insert': (array, num, index) => {
            array.splice(+index, 0, +num);
        }
    }

    data.forEach(data => {
        let [command, num, index] = data.split(' ');
        manipulations[command](nums, num, index)
    });

    console.log(nums.join(' '));
}

arrayManipulations(['4 19 2 53 6 43',
    'Add 3',
    'Remove 2',
    'RemoveAt 1',
    'Insert 8 3']
);


// 4 53 6 8 43 3

arrayManipulations(['6 12 2 65 6 42',
    'Add 8',
    'Remove 12',
    'RemoveAt 3',
    'Insert 6 2']
);

// 6 2 6 65 42 8