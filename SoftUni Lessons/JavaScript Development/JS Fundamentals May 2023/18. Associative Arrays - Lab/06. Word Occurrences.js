function mask (params) {
    // MASK
    const occurrences = params.reduce(function (acc, curr) {
        return acc[curr] ? ++acc[curr] : acc[curr] = 1, acc},
        {});

    let sorted = Object.keys(occurrences)
        .sort((a, b) => occurrences[b] - occurrences[a])

    sorted.forEach(word => {
        console.log(`${word} -> ${occurrences[word]} times`);
    });
}

mask(["Here", "is", "the", "first", "sentence",
"Here", "is", "another", "sentence", "And",
"finally", "the", "third", "sentence"]);
// sentence -> 3 times
// Here -> 2 times
// is -> 2 times
// the -> 2 times
// first -> 1 times
// another -> 1 times
// And -> 1 times
// finally -> 1 times
// third -> 1 times

console.log('-------------------------------------');

mask(["dog", "bye", "city", "dog", "dad",
"boys", "ginger"]);
// dog -> 2 times
// bye -> 1 times
// city -> 1 times
// dad -> 1 times
// boys -> 1 times
// ginger -> 1 times
