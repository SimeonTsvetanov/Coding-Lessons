function arrayManipulator (...params) {
    // MASK
    let [nums, commands] = params;

    for (let i = 0; i < commands.length; i++) {
        let x = commands[i];
        let data = x.split(' ');
        const command = data.shift();

        if (command === 'add') {
            const [index, element] = data.map(Number)
            nums.splice(index, 0, element);
        } else if (command === 'addMany') {
            const index = Number(data.shift())
            const elements = data.map(Number)
            nums.splice(index, 0, ...elements);
        } else if (command === 'contains') {
            const element = Number(data.shift());
            console.log(nums.indexOf(element));
        } else if (command === 'remove') {
            const index = Number(data.shift());
            nums.splice(index, 1);
        } else if (command === 'shift') {
            const positions = Number(data.shift());
            for (let position = 1; position <= positions; position += 1) {
                nums.push(nums.shift());
            }
        } else if (command === 'sumPairs') {
            const result = [];
            for (let i = 0; i < nums.length; i += 2) {
                if (i + 1 < nums.length) {
                    const sum = nums[i] + nums[i + 1];
                    result.push(sum);
                } else {
                    result.push(nums[i]);
                }
            }
            nums = result;
        } else if (command === 'print') {
            console.log(`[ ${nums.join(', ')} ]`);
            break;
        }
    }
}

arrayManipulator([1, 2, 4, 5, 6, 7],
['add 1 8', 'contains 1', 'contains 3', 'print']);
// 0
// -1
// [ 1, 8, 2, 4, 5, 6, 7 ]

console.log('-------------------------------------');

arrayManipulator([1, 2, 3, 4, 5],
['addMany 5 9 8 7 6 5', 'contains 15', 'remove 3',
'shift 1', 'print']
);
// -1
// [ 2, 3, 5, 9, 8, 7, 6,
// 5, 1 ]
