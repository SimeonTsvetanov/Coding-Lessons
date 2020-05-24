function printAnArrayWithAGivenDelimiter(array) {
    // Mask
    let delimiter = array.pop();
    console.log(array.join(`${delimiter}`))
}

printAnArrayWithAGivenDelimiter([
    'One',
    'Two',
    'Three',
    'Four',
    'Five',
    '-'
]);
// Should return: One-Two-Three-Four-Five

printAnArrayWithAGivenDelimiter([
    'How about no?',
    'I',
    'will',
    'not',
    'do',
    'it!',
    '_'
]);
// Should return: How about no?_I_will_not_do_it!