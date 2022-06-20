function arrayManipulator (nums, commands) {
    // MasK
    let insert = (array, index, element) => {
        return array.splice(index, 0, element);
    }

    let removeAt = (array, index) => {
        return array.splice(index, 1);
    }

    commands.forEach(data => {
        data = data.split(' ');
        const command = data.shift();
        if (command === 'add') {
            insert(nums, +data.shift(), +data.shift())
        } else if (command === 'addMany') {
            let index = +data.shift();
            nums.splice(index, 0, ...data.map(Number));
        } else if (command === 'contains') {
            console.log(nums.indexOf(+data.shift()));
        } else if (command === 'remove') {
            removeAt(nums, +data.shift());
        } else if (command === 'shift') {
            let positions = +data.shift();
            for (let i = 0; i < positions; i++) {
                let num = nums.shift();
                nums.push(num);
            }
        } else if (command === 'sumPairs') {
            let pairs = [];
            for (let i = 0; i < nums.length; i += 2) {
                let a = nums[i];
                let b = i + 1 < nums.length ? nums[i + 1] : 0;
                pairs.push(a + b);
            }
            nums = pairs;
        } else if (command === 'print') {
            console.log(`[ ${nums.join(', ')} ]`);
            return;
        }
    });
}

// arrayManipulator([1, 2, 4, 5, 6, 7],
//     ['add 1 8', 'contains 1', 'contains 3', 'print']
// );

// 0
// -1
// [ 1, 8, 2, 4, 5, 6, 7 ]

console.log('------------------');

arrayManipulator([1, 2, 3, 4, 5],
    ['addMany 5 9 8 7 6 5', 'contains 15', 'remove 3', 'shift 1', 'print']
);

// -1
// [ 2, 3, 5, 9, 8, 7, 6, 5, 1 ]

