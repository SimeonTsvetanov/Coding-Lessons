function club(input) {
    // Mask
    let aim = Number(input.shift());
    let income = 0;

    while('Party or Aim') {
        let cocktail = input.shift();
        if (cocktail == 'Party!') {  // Sad story
            console.log(`We need ${(aim - income).toFixed(2)} leva more.`);
            break;
        }
        let count = Number(input.shift());
        
        let price = cocktail.length * count;
        if (price % 2 != 0) {price *= 0.75;}  // Cheap-ass
        
        income += price;

        if (income >= aim) {  // You ruch bru!
            console.log(`Target acquired.`);
            break;
        }
    }

    console.log(`Club income - ${income.toFixed(2)} leva.`);
}

club([500, 'Bellini', 6, 'Bamboo', 7, 'Party!']);  // Should return:
// We need 416.00 leva more.
// Club income - 84.00 leva.

club([100, 'Sidecar', 7, 'Mojito', 5, 'White Russian', 10]);  // Should return:
// Target acquired.
// Club income - 196.75 leva.
