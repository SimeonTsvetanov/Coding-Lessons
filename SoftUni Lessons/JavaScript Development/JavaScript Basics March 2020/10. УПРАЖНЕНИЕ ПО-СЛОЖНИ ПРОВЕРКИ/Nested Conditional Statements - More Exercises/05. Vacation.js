function vacantion(...input) {
    let budget = Number(input.shift());
    let season = input.shift();  // Winter or Summer

    let accommodation = undefined;  // Hotel, Hut or Camp
    let location = undefined;  // Alaska or Morocco
    let price = undefined;  // Only god knows

    if (budget <= 1000) {
        accommodation = "Camp";
        switch (season) {
            case "Summer":
                location = "Alaska";
                price = budget * 0.65;
                break;
            case "Winter":
                location = "Morocco";
                price = budget * 0.45;
        }
    } else if (budget > 1000 && budget <= 3000) {
        accommodation = "Hut";
        switch (season) {
            case "Summer":
                location = "Alaska";
                price = budget * 0.80;
                break;
            case "Winter":
                location = "Morocco";
                price = budget * 0.60;
        }
    } else {
        accommodation = "Hotel";
        price = budget * 0.9;
        switch (season) {
            case "Summer":
                location = "Alaska";
                break;
            case "Winter":
                location = "Morocco";
        }
    }

    console.log(`${location} - ${accommodation} - ${price.toFixed(2)}`);
}


vacantion(['800', 'Summer']);  // Expected Output:
// Alaska - Camp - 520.00

vacantion(['799.50', 'Winter']);  // Expected Output:
// Morocco - Camp - 359.78

vacantion(['3460', 'Summer']);  // Expected Output:
// Alaska - Hotel - 3114.00

vacantion(['1100', 'Summer']);  // Expected Output:
// Alaska - Hut - 880.00

vacantion(['5000', 'Winter']);  // Expected Output:
// Morocco - Hotel - 4500.00

vacantion(['2543.99', 'Winter']);  // Expected Output:
// Morocco - Hut - 1526.39