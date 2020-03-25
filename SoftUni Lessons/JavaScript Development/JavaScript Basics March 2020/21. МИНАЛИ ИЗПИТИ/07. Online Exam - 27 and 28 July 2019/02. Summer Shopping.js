function summerShopping(params) {
    let budget = Number(params.shift());
    let priceTowel = Number(params.shift());
    let discount = Number(params.shift());

    let priceUmbrella = (priceTowel / 3) * 2;
    let priceSandals = priceUmbrella * 0.75;
    let priceBag = (priceTowel + priceSandals) / 3;

    let price = priceTowel + priceUmbrella + priceSandals + priceBag;
    let dis = (discount * price) / 100;
    price -= dis

    if (budget >= price) {
        console.log(`Annie's sum is ${price.toFixed(2)} lv. She has ${(budget - price).toFixed(2)} lv. left.`);
    } else {
        console.log(`Annie's sum is ${price.toFixed(2)} lv. She needs ${(price - budget).toFixed(2)} lv. more.`);
    }
}


summerShopping([40, 15, 5]);  // Expected Output:
// Annie's sum is 38.00 lv. She has 2.00 lv. left.

summerShopping([25, 6, 10]);  // Expected Output:
// Annie's sum is 14.40 lv. She has 10.60 lv. left.

summerShopping([30, 17, 3]);  // Expected Output:
// Annie's sum is 43.97 lv. She needs 13.97 lv. more.
