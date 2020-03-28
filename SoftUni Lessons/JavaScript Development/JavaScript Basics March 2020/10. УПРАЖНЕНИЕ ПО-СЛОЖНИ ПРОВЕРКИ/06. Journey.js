function journey(...input) {
    let budget = Number(input.shift());
    let season = input.shift();

    let location = '';
    let accommodation = '';
    let price = 0;

    switch (season) {
        case "summer": accommodation = "Camp"; break;
        case "winter": accommodation = "Hotel";
    }

    if (budget <= 100) {
        location = "Bulgaria";
        switch (season) {
            case "summer": price = budget * 0.3; break;
            case "winter": price = budget * 0.7;
        }
    } else if (budget > 100 && budget <= 1000) {
        location = "Balkans";
        switch (season) {
            case "summer": price = budget * 0.4; break;
            case "winter": price = budget * 0.8;
        } 
    } else if (budget > 1000) {
        location = "Europe";
        accommodation = "Hotel";
        price = budget * 0.9;
    }

    console.log(`Somewhere in ${location}`);
    console.log(`${accommodation} - ${price.toFixed(2)}`);
}

journey(['50', 'summer']);  // Expected Output:
// Somewhere in Bulgaria
// Camp - 15.00

journey(['75', 'winter']);  // Expected Output:
// Somewhere in Bulgaria
// Hotel - 52.50

journey(['312', 'summer']);  // Expected Output:
// Somewhere in Balkans
// Camp - 124.80

journey(['678.53', 'winter']);  // Expected Output:
// Somewhere in Balkans
// Hotel - 542.82

journey(['1500', 'summer']);  // Expected Output:
// Somewhere in Europe
// Hotel - 1350.00

