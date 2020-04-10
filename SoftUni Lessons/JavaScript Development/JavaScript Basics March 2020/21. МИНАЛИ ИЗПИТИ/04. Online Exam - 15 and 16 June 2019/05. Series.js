function series(input) {
    // Mask
    let discounted = {
        'Thrones': 0.5,
        'Lucifer': 0.6,	
        'Protector': 0.7,
        'TotalDrama': 0.8,
        'Area': 0.9
    };
    
    let budget = Number(input.shift());
    let count = Number(input.shift());

    for (let serial = 1; serial <= count; serial += 1) {
        let name = input.shift();
        let price = Number(input.shift());
        if (name in discounted) {price *= discounted[name];}
        budget -= price;
    }

    if (budget >= 0) {
        console.log(`You bought all the series and left with ${budget.toFixed(2)} lv.`);
    } else {
        console.log(`You need ${Math.abs(budget).toFixed(2)} lv. more to buy the series!`);
    }
}

series([10, 3, 'Thrones', 5, 'Riverdale', 5, 'Gotham', 2]);  // Should return:
// You bought all the series and left with 0.50 lv.

series([25, 6, 'Teen Wolf', 8, 'Protector', 5, 'TotalDrama', 5, 'Area', 4, 'Thrones', 5, 'Lucifer', 9]);  
// Should return:
// You need 2.00 lv. more to buy the series!