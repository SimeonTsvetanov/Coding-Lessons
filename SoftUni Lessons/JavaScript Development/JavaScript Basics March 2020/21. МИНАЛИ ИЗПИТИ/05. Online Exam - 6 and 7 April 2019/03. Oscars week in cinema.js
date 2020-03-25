function oscarsWeekInCinema(params) {
    let name = params.shift();
    let room = params.shift();
    let tickets = Number(params.shift());

    let prices = {
        'A Star Is Born': {'normal': 7.50, 'luxury': 10.50, 'ultra luxury': 13.50},
        'Bohemian Rhapsody': {'normal': 7.35, 'luxury': 9.45, 'ultra luxury': 12.75},
        'Green Book': {'normal': 8.15, 'luxury': 10.25, 'ultra luxury': 13.25},
        'The Favourite': {'normal': 8.75, 'luxury': 11.55, 'ultra luxury': 13.95}
    };

    let price = prices[name][room] * tickets;

    console.log(`${name} -> ${price.toFixed(2)} lv.`);
}


oscarsWeekInCinema(['A Star Is Born', 'luxury', '42']);  // Expected Output:
// A Star Is Born -> 441.00 lv.

oscarsWeekInCinema(['Green Book', 'normal', '63']);  // Expected Output:
// Green Book -> 513.45 lv.

oscarsWeekInCinema(['The Favourite', 'ultra luxury', '34']);  // Expected Output:
// The Favourite -> 474.30 lv.