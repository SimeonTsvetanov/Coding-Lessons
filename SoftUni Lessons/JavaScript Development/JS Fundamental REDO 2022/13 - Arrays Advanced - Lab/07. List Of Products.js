function listOfProducts (array) {
    // MasK
    array.sort().forEach((product, number) => {
        console.log(`${number + 1}.${product}`);
    });
}

listOfProducts(['Potatoes', 'Tomatoes', 'Onions', 'Apples']);

// 1.Apples
// 2.Onions
// 3.Potatoes
// 4.Tomatoes
