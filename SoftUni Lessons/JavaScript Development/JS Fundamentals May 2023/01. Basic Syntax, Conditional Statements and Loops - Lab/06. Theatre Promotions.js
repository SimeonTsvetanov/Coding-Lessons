function mask (...params) {
    // MASK
    [day, age] = params;

    let prices = {
        "Weekday": [12, 18, 12],
        "Weekend": [15, 20, 15],
        "Holiday": [5, 12, 10]
    };

    let price;

    if (age >= 0 && age <= 18) { price = prices[day][0]; }
    else if (age > 18 && age <= 64) { price = prices[day][1]; }
    else if (age > 64 && age <= 122) { price = prices[day][2]; }

    (price) ? console.log(`${price}$`) : console.log('Error!');
}

mask('Weekday', 42);
// 18$

mask('Holiday', -12);
// Error!

mask('Holiday', 15);
// 5$
