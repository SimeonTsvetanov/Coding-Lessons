function movieDestination(params) {
    let budget = Number(params.shift());
    let destination = params.shift();
    let season = params.shift();
    let days = Number(params.shift());

    let prices = {
        'Dubai': {'Winter': 45000, 'Summer': 40000},
        'Sofia': {'Winter': 17000, 'Summer': 12500},
        'London': {'Winter': 24000, 'Summer': 20250}
    };

    let price = prices[destination][season] * days;
    
    if (destination == "Dubai") {
        price *= 0.7;
    } else if (destination == "Sofia") {
        price *= 1.25;
    }

    if (price <= budget) {
        console.log(`The budget for the movie is enough! We have ${Math.abs(price - budget).toFixed(2)} leva left!`);
    } else {
        console.log(`The director needs ${Math.abs(budget - price).toFixed(2)} leva more!`);
    }
}


movieDestination(['400000', 'Sofia', 'Winter', '20']);  // Expected Output:
// The director needs 25000.00 leva more!

movieDestination(['1000000', 'Dubai', 'Summer', '5']);  // Expected Output:
// The budget for the movie is enough! We have 860000.00 leva left!

movieDestination(['200000', 'London', 'Summer', '7']);  // Expected Output:
// The budget for the movie is enough! We have 58250.00 leva left!