function wordOccurrences(input) {
    // Mask
    let dict = new Map();

    for (let word of input) {
        dict.has(word) ? dict.set(word, dict.get(word) + 1) : dict.set(word, 1);
    }
    
    let sorted = Array.from(dict.entries()).sort((a, b) => b[1] - a[1]);
    for (let [word, count] of sorted) {
        console.log(`${word} -> ${count} times`);
    }
}

wordOccurrences([
    "Here", "is", "the", "first", "sentence",
    "Here", "is", "another", "sentence", "And",
    "finally", "the", "third", "sentence"
]);
// Should return:
// sentence -> 3 times
// Here -> 2 times
// is -> 2 times
// the -> 2 times
// first -> 1 times
// another -> 1 times
// And -> 1 times
// finally -> 1 times
// third -> 1 times
