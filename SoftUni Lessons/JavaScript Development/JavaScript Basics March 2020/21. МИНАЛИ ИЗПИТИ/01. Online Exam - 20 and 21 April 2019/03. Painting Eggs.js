function paintingEggs(params) {
    let size = params.shift();
    let color = params.shift();
    let count = Number(params.shift());

    let prices = {
        'Large': {'Red': 16, 'Green': 12, 'Yellow': 9},
        'Medium': {'Red': 13, 'Green': 9, 'Yellow': 7},
        'Small': {'Red': 9, 'Green': 8, 'Yellow': 5}
    };

    console.log(`${((prices[size][color] * count) * 0.65).toFixed(2)} leva.`)
}

paintingEggs(['Large', 'Red', '7'])  // Expected Output: 72.80 leva.
paintingEggs(['Medium', 'Green', '5'])  // Expected Output: 29.25 leva.
paintingEggs(['Small', 'Yellow', '3'])  // Expected Output: 9.75 leva.
