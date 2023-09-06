function mask (...params) {
    // MASK
    let group = params.shift();
    let type = params.shift();
    let day = params.shift();

    let prices = {
        'Students': {
            'Friday': 8.45,
            'Saturday': 9.80,
            'Sunday': 10.46
        },
        'Business': {
            'Friday': 10.90,
            'Saturday': 15.60,
            'Sunday': 16
        },
        'Regular': {
            'Friday': 15,
            'Saturday': 20,
            'Sunday': 22.50
        }
    }

    let total = prices[type][day];

    if (type === 'Students' && group >= 30) {total *= 0.85}
    if (type === 'Business' && group >= 100) {group -= 10}
    if (type === 'Regular' && group >= 10 && group <= 20) {total *= 0.95}

    console.log(`Total price: ${(total * group).toFixed(2)}`);
}

mask(30,
"Students",
"Sunday"
);
// Total price: 266.73

mask(40,
"Regular",
"Saturday"
);
// Total price: 800.00
