function GodzillaVsKong(input) {
    let budget = Number(input.shift());
    let countStatists = Number(input.shift());
    let priceOneDress = Number(input.shift());

    let decor = budget * 0.1;
    let dresses = countStatists * priceOneDress;

    if (countStatists > 150) {
        dresses *= 0.9;
    }

    let total = decor + dresses;

    let difference = (Math.abs(total - budget)).toFixed(2);

    if (total > budget) {
        console.log(`Not enough money!`);
        console.log(`Wingard needs ${difference} leva more.`);
    } else {
        console.log(`Action!`);
        console.log(`Wingard starts filming with ${difference} leva left.`);
    }
}

GodzillaVsKong(["20000", "120", "55.5"]);
// Expexted output:
// Action!
// Wingard starts filming with 11340.00 leva left.

GodzillaVsKong(["15437.62", "186", "57.99"]);
// Expected Output:
// Action!
// Wingard starts filming with 4186.33 leva left.

GodzillaVsKong(["9587.88", "222", "55.68"]);
// Expected Output:
// Not enough money!
// Wingard needs 2495.77 leva more.
