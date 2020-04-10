function careOfPuppy(input) {
    // Mask
    let food = Number(input.shift()) * 1000;

    while('Adopted') {
        let command = input.shift();
        if (command == 'Adopted') {break;}
        food -= Number(command);
    }

    if (food >= 0) {console.log(`Food is enough! Leftovers: ${food} grams.`);}
    else {console.log(`Food is not enough. You need ${Math.abs(food)} grams more.`)}
}

careOfPuppy([4, 130, 345, 400, 180, 230, 120, 'Adopted']);  // Should return:
// Food is enough! Leftovers: 2595 grams.

careOfPuppy([3, 1000, 1000, 1000, 'Adopted']);  // Should return:
// Food is not enough. You need 2032 grams more.
