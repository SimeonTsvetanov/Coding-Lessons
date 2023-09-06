function mask (num) {
    // MASK
    let positiveDividers = []

    for(let i = 1; i < num; i++) {
        (num % i === 0) ? positiveDividers.push(i) : 'pass';
    }

    (positiveDividers.reduce((a, b) => a + b, 0) === num)
        ? console.log('We have a perfect number!')
        : console.log('It\'s not so perfect.');
}

mask(6);
// We have a perfect number!

console.log('-------------------------------------');

mask(1236498);
// It's not so perfect.
