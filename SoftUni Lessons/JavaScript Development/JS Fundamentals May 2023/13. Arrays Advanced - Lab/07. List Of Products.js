function mask (products) {
    // MASK
    products.sort().forEach((product, index) => {
        console.log(`${index + 1}.${product}`);
    });
}

mask(['Potatoes', 'Tomatoes', 'Onions', 'Apples']);
// 1.Apples
// 2.Onions
// 3.Potatoes
// 4.Tomatoes

console.log('-------------------------------------');

mask(['Watermelon', 'Banana', 'Apples']);
// 1.Apples
// 2.Banana
// 3.Watermelon
