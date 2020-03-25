function shopping(params) {
    let budget = Number(params.shift());
    let countVideoCards = Number(params.shift());
    let countProcessors = Number(params.shift());
    let countRam = Number(params.shift());

    let priceVideoCards = 250 * countVideoCards;
    let priceProcessors = (priceVideoCards * 0.35) * countProcessors;
    let priceRam = (priceVideoCards * 0.1) * countRam;

    let price = priceVideoCards + priceProcessors + priceRam

    if (countVideoCards > countProcessors) {
        price *= 0.85;
    }

    if (budget >= price) {
        console.log(`You have ${(budget - price).toFixed(2)} leva left!`);
    } else {
        console.log(`Not enough money! You need ${(price - budget).toFixed(2)} leva more!`);
    }
}


shopping([900, 2, 1, 3]);  // Expected Output:
// You have 198.75 leva left!

shopping([920.45, 3, 1, 1]);  // Expected Output:
// Not enough money! You need 3.92 leva more!