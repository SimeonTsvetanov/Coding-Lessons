function addAndRemoveElements(commands) {
    // Mask
    let array = [];
    let number = 1;
    commands.forEach((command, index) => {
        command === 'add' ? array.push(number) : array.pop();
        number++;
    })
    array.length > 0 ? console.log(array.join('\n')) : console.log('Empty');
}

addAndRemoveElements([
    'add',
    'add',
    'add',
    'add'
]);
// Should return:
// 1
// 2
// 3
// 4


addAndRemoveElements([
    'add',
    'add',
    'remove',
    'add',
    'add'
]);
// Should return:
// 1
// 4
// 5
