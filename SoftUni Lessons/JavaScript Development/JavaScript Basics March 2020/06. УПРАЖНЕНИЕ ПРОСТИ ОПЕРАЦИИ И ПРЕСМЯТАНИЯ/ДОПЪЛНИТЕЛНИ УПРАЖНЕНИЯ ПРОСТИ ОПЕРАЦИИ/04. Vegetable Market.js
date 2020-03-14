// There are two ways to test the task in Judge
// This is the new way:
function vegetableMarket(priceKgVegetables, priceKgFruits, totalKgVegetables, totalKgFruits) {
    let total = (((priceKgVegetables * totalKgVegetables) + (priceKgFruits * totalKgFruits)) / 1.94).toFixed(2);
    console.log(total);
}

vegetableMarket(0.194, 19.4, 10, 10);  // Expected output: 101.00
vegetableMarket(1.5, 2.5, 10, 10);  // Expected output: 20.62

// -----------------------------------------------------------------------------------//
// Old way of reading the input:
function vegetableMarket(input) {
    let priceKgVegetables = Number(input.shift());
    let priceKgFruits = Number(input.shift());
    let totalKgVegetables = Number(input.shift());
    let totalKgFruits = Number(input.shift());
    let total = (((priceKgVegetables * totalKgVegetables) + (priceKgFruits * totalKgFruits)) / 1.94).toFixed(2);
    console.log(total);
}
vegetableMarket([0.194, 19.4, 10, 10]);  // Expected output: 101.00
vegetableMarket([1.5, 2.5, 10, 10]);  // Expected output: 20.62
