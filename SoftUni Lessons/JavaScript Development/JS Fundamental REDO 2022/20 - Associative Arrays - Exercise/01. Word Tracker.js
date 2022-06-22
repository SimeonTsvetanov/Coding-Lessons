function legendaryFarming (wordsPool) {
    // MasK
    class Word {
        constructor(word, count) {
            this.word = word;
            this.count = count;
        }

        print () {
            return `${this.word} - ${this.count}`;
        }
    }

    let words = [];

    let wordsToSearchFor = wordsPool.shift().split(' ');
    wordsToSearchFor.forEach(word => {
        let count = wordsPool.filter(searchedWord => word === searchedWord).length;
        words.push(new Word(word, count));
    });

    words.sort((a, b) => b.count - a.count);
    words.forEach(word => {
        console.log(word.print());
    });
}

legendaryFarming([
        'this sentence',
        'In', 'this', 'sentence', 'you', 'have', 'to', 'count', 'the', 'occurrences', 'of', 'the', 'words', 'this', 'and', 'sentence', 'because', 'this', 'is', 'your', 'task'
    ]
);

// this - 3
// sentence - 2


console.log();

legendaryFarming([
    'is the',
    'first', 'sentence', 'Here', 'is', 'another', 'the', 'And', 'finally', 'the', 'the', 'sentence']
);

// the – 3
// is - 1
