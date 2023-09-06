function mask (params) {
    // MASK
    let searched = Object.fromEntries( params.shift().split(' ').map( x => [x, 0]) );
    params.forEach(word => {
        (word in searched) ? searched[word] += 1 : 'pass';
    });


    Object.entries(searched)
        .sort((a, b) => b[1] - a[1])
        .forEach(word => {
            console.log(`${word[0]} - ${word[1]}`);
    });
}

mask([
'this sentence',
'In', 'this', 'sentence', 'you', 'have',
'to', 'count', 'the', 'occurrences', 'of',
'the', 'words', 'this', 'and', 'sentence',
'because', 'this', 'is', 'your', 'task'
]
);
// this - 3
// sentence - 2

console.log('-------------------------------------');

mask([
'is the',
'first', 'sentence', 'Here', 'is',
'another', 'the', 'And', 'finally', 'the',
'the', 'sentence']);
// the – 3
// is - 1
