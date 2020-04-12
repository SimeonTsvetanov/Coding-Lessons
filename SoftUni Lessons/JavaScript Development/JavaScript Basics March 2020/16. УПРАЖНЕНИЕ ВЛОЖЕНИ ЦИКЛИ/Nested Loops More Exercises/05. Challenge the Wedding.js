function challengeTheWedding(input) {
    // Mask
    let men = Number(input.shift());
    let women = Number(input.shift());
    let max = Number(input.shift());

    let orgy = ''

    for (let man = 1; man <= men; man += 1) {
        if (max == 0) {break;}
        for (woman = 1; woman <= women; woman += 1) {
            orgy += `(${man} <-> ${woman}) `;
            max -= 1
            if (max == 0) {break;}  // Condoms over
        }
    }

    console.log(orgy);  // logging the orgy is called porn...
}

challengeTheWedding([2, 2, 6]);  // Should return:
// (1 <-> 1) (1 <-> 2) (2 <-> 1) (2 <-> 2)

challengeTheWedding([2, 2, 3]);  // Should return:
// (1 <-> 1) (1 <-> 2) (2 <-> 1) 