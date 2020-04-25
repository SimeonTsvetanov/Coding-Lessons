function listOfProducts(array) {
    // Mask
    let products = array.slice()  // We copy the array
        .sort()  // Sort it alphabetically
        .map((product, index) => `${index + 1}.${product}`);  // Add numeration of the products
    console.log(products.join('\n'));  // Print each element on a new line
}

listOfProducts(["Potatoes", "Tomatoes", "Onions", "Apples"]);
// Should return:

// 1.Apples
// 2.Onions
// 3.Potatoes
// 4.Tomatoes
