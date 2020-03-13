function cinema(input) {
    let projectionType = input.shift();
    let rows = Number(input.shift());
    let cols = Number(input.shift());

    let price = 0;

    switch(projectionType) {
        case "Premiere":
            price = rows * cols * 12; break;
        case "Normal":
            price = rows * cols * 7.5; break;
        case "Discount":
            price = rows * cols * 5.00; break;
    }

    console.log(`${price.toFixed(2)} leva`);
}

cinema(['Premiere', '10', '12']);  // Expected Output: 1440.00 leva
cinema(['Normal', '21', '13']);  // Expected Output: 2047.50 leva
cinema(['Discount', '12', '30']);  // Expected Output: 1800.00 leva