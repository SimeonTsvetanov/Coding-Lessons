function filmPremiere(params) {
    let movie = params.shift();
    let packet = params.shift();
    let countTickets = Number(params.shift());

    let prices = {
        'John Wick': {'Drink': 12, 'Popcorn': 15, 'Menu': 19},
        'Star Wars': {'Drink': 18, 'Popcorn': 25, 'Menu': 30},
        'Jumanji': {'Drink': 9, 'Popcorn': 11, 'Menu': 14}
    };

    let price = prices[movie][packet] * countTickets;

    if (movie == 'Star Wars' && countTickets >= 4) {
        price *= 0.7;
    } else if (movie == 'Jumanji' && countTickets == 2) {
        price *= 0.85;
    }

    console.log(`Your bill is ${price.toFixed(2)} leva.`);
}


filmPremiere(['John Wick', 'Drink', '6']);  // Expected Output:
// Your bill is 72.00 leva.

filmPremiere(['Star Wars', 'Popcorn', '4']);  // Expected Output:
// Your bill is 70.00 leva.

filmPremiere(['Jumanji', 'Menu', '2']);  // Expected Output:
// Your bill is 23.80 leva.
