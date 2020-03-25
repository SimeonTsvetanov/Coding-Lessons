function godzillaVsKong(params) {
    let budget = Number(params.shift());
    let people = Number(params.shift());
    let priceForOne = Number(params.shift());

    let decor = budget * 0.1;
    
    if (people > 150) {
        priceForOne *= 0.9
    }

    let price = (people * priceForOne) + decor;
    let difference = Math.abs(budget - price);

    if (price > budget) {
        console.log(`Not enough money!`);
        console.log(`Wingard needs ${difference.toFixed(2)} leva more.`);
    } else {
        console.log(`Action!`);
        console.log(`Wingard starts filming with ${difference.toFixed(2)} leva left.`);
    }
}


godzillaVsKong(['20000', '120', '55.5']);  // Expected Output:
// Action!
// Wingard starts filming with 11340.00 leva left.

godzillaVsKong(['15437.62', '186', '57.99']);  // Expected Output:
// Action!
// Wingard starts filming with 4186.33 leva left.

godzillaVsKong(['9587.88', '222', '55.68']);  // Expected Output:
// Not enough money!
// Wingard needs 2495.77 leva more.