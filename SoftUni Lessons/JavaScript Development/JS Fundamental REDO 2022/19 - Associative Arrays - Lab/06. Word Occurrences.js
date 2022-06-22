function wordOccurrences (inputWords) {
    // MasK
    function sortObject(obj) {
        let sortedKVP = Array.from(Object.entries(obj)).sort((a, b) => {
            // Example Sort buy value (NUMBER) the smallest FIRST
            return b[1] - a[1] || 'if you want a second condition';
        });
        let sortedObject = {}
        for (let i = 0; i < sortedKVP.length; i ++) {
            sortedObject[sortedKVP[i][0]] = sortedKVP[i][1]
        }
        return sortedObject;
    }

    function countOccurrences(array, word) {
        return array.filter(w => w === word).length;
    }

    let words = {};

    inputWords.forEach(word => {
        words[word] = countOccurrences(inputWords, word);
    });

    let sortedWords = sortObject(words);
    for (const [word, count] of Object.entries(sortedWords)) {
        console.log(`${word} -> ${count} times`);
    }
}

wordOccurrences(["Here", "is", "the", "first", "sentence", "Here", "is", "another", "sentence", "And", "finally", "the", "third", "sentence"]);

// sentence -> 3 times
// Here -> 2 times
// is -> 2 times
// the -> 2 times
// first -> 1 times
// another -> 1 times
// And -> 1 times
// finally -> 1 times
// third -> 1 times
