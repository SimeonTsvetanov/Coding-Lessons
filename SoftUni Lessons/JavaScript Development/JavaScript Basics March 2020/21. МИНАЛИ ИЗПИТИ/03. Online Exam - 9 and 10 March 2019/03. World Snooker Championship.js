function worldSnookerChampionship(params) {
    let period = params.shift();
    let ticket = params.shift();
    let count = Number(params.shift());
    let picture = params.shift();

    let prices = {
        'Quarter final': { 'Standard': 55.50, 'Premium': 105.20, 'VIP': 118.90 },
        'Semi final': { 'Standard': 75.88, 'Premium': 125.22, 'VIP': 300.40 },
        'Final': { 'Standard': 110.10, 'Premium': 160.66, 'VIP': 400 }
    };

    let price = prices[period][ticket] * count;

    if (price > 4000) {
        price *= 0.75;
        picture = 'N';
    } else if (price > 2500) {
        price *= 0.9;
    }

    if (picture == 'Y') {
        price += 40 * count;
    } 
    
    console.log(price.toFixed(2));
}


worldSnookerChampionship(['Final', 'Premium', '25', 'Y']);
// Expected Output: 3012.38

worldSnookerChampionship(['Semi final', 'VIP', '9', 'Y']);
// Expected Output: 2793.24

worldSnookerChampionship(['Quarter final', 'Standard', '11', 'N']);
// Expected Output: 610.50
