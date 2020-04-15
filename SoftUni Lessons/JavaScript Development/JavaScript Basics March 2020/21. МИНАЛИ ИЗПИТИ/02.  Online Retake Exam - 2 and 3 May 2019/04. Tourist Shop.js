// Късо линкче: https://git.io/JfvMz

function touristShop(input) {
    // Mask
    let budget = Number(input.shift());
    let products = 0;
    let total = 0;

    while('I am an idiot!') {
        let product = input.shift(); 
        if (product == 'Stop') {
            console.log(`You bought ${products} products for ${total.toFixed(2)} leva.`);
            break;
        }
        products += 1;
        let price = Number(input.shift());
        if (products % 3 == 0) {
            price = price / 2;
        }

        if (budget - price < 0) {
            console.log(`You don't have enough money!`);
            console.log(`You need ${(price - budget).toFixed(2)} leva!`);
            break;
        }
        
        total += price;
        budget -= price;
    }
}

touristShop([153.20, 'Backpack', 25.20, 'Shoes', 54, 'Sunglasses', 30, 'Stop']);  // Should return:
// You bought 3 products for 94.20 leva.

touristShop([54, 'Thermal underwear', 24, 'Sunscreen', 45]);  // Should return:
// You don't have enough money!
// You need 15.00 leva!
