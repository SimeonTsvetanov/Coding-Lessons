function wordsTracker(input) {
    // Mask
    let words = {};
    input.shift().split(' ').map(word => words[word] = 0);

    input.map(word => {
        words.hasOwnProperty(word) ? words[word] += 1 : 'pass';
    });

    Object.entries(words).sort((a, b) => b[1] - a[1]).forEach(word => {
        console.log(`${word[0]} - ${word[1]}`);
    })
}


wordsTracker([
        'this sentence',
        'In','this','sentence','you','have','to','count','the','occurances','of','the'
        ,'words','this','and','sentence','because','this','is','your','task'
]);
// Should return:
// this - 3
// sentence - 2
