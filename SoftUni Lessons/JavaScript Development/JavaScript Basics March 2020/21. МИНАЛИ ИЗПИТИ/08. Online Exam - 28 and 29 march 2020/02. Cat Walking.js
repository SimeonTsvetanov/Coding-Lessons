function catWalk(input) {
    // Mask

    // Sorry but I had to add it:

    // 'Cause I'm a model, you know what I mean
    // And I do my little turn on the CATWALK
    // Yeah, on the CATWALK
    // On the CATWALK, yeah
    // I shake my little tush on the CATWALK

    // I'm too sexy for my car
    // Too sexy for my car
    // Too sexy by far
    // And I'm too sexy for my hat
    // Too sexy for my hat
    // What do you think about that?

    let spendCalories = Number(input.shift()) * Number(input.shift()) * 5;
    let neededCalories = Number(input.shift()) / 2;

    if (spendCalories >= neededCalories) {
        console.log(`Yes, the walk for your cat is enough. Burned calories per day: ${spendCalories}.`);
    } else {
        console.log(`No, the walk for your cat is not enough. Burned calories per day: ${spendCalories}.`);
    }
}

catWalk([30, 3, 600]);  // Should return:
// Yes, the walk for your cat is enough. Burned calories per day: 450.

catWalk([15, 2, 500]);  // Should return:
// No, the walk for your cat is not enough. Burned calories per day: 150.