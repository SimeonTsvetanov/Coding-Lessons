function easterBake(input) {
    // Mask
    let count = Number(input.shift());

    let maxFlour = 0;
    let maxSugar = 0;

    let totalSugar = 0;
    let totalFlour = 0;

    for (let bread = 1; bread <= count; bread += 1) {
        let sugar = Number(input.shift());
        if (sugar > maxSugar) {maxSugar = sugar;}
        totalSugar += sugar;

        let flour = Number(input.shift());
        if (flour > maxFlour) {maxFlour = flour;}
        totalFlour += flour;
    }

    console.log(`Sugar: ${Math.ceil(totalSugar / 950)}`);
    console.log(`Flour: ${Math.ceil(totalFlour / 750)}`);
    console.log(`Max used flour is ${maxFlour} grams, max used sugar is ${maxSugar} grams.`);
}

easterBake([3, 400, 350, 250, 300, 450, 380,]);  // Should return:
// Sugar: 2
// Flour: 2
// Max used flour is 380 grams, max used sugar is 450 grams.

easterBake([4, 500, 350, 560, 430, 600, 345, 578, 543]);  // Should return:
// Sugar: 3
// Flour: 3
// Max used flour is 543 grams, max used sugar is 600 grams.
