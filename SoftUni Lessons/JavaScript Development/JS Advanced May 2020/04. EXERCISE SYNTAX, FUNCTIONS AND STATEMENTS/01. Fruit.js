function fruit(fruit, weight, price) {
    // Mask
    console.log(`I need $${(price * weight / 1000).toFixed(2)} to buy ${(weight / 1000).toFixed(2)} kilograms ${fruit}.`);
}

fruit('orange', 2500, 1.80);  // Should return:
// I need $4.50 to buy 2.50 kilograms orange.

fruit('apple', 1563, 2.35);  // Should return:
// I need $3.67 to buy 1.56 kilograms apple.