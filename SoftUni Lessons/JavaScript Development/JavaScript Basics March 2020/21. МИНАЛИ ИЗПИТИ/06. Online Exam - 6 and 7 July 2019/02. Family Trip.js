function familyTrip(params) {
    let budget = Number(params.shift());
    let countNights = Number(params.shift());
    let priceNights = Number(params.shift());
    let extraExpenses = Number(params.shift());

    if (countNights > 7) { 
        priceNights *= 0.95; 
    }

    let price = (priceNights * countNights) + ((extraExpenses * budget) / 100); 
    
    if (budget >= price) {
        console.log(`Ivanovi will be left with ${(budget - price).toFixed(2)} leva after vacation.`);
    } else {
        console.log(`${(price - budget).toFixed(2)} leva needed.`);
    }
}


familyTrip([800.50, 8, 100, 2]);  // Expected Output:
// Ivanovi will be left with 24.49 leva after vacation.

familyTrip([500, 7, 66, 15]);  // Expected Output:
// 37.00 leva needed.