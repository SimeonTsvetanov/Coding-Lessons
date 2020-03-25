function travelAgency(params) {
    let city = params.shift();
    let pack = params.shift();
    let vip = params.shift();
    let days = Number(params.shift());

    if (days > 7) {
        days -= 1;
    }

    let prices = {
        'Bansko': {'withEquipment': {'price': 100, 'yes': 0.9, 'no': 1}, 'noEquipment': {'price': 80, 'yes': 0.95, 'no': 1}},
        'Borovets': {'withEquipment': {'price': 100, 'yes': 0.9, 'no': 1}, 'noEquipment': {'price': 80, 'yes': 0.95, 'no': 1}},
        'Varna': {'withBreakfast': {'price': 130, 'yes': 0.88, 'no': 1}, 'noBreakfast': {'price': 100, 'yes': 0.93, 'no': 1}},
        'Burgas': {'withBreakfast': {'price': 130, 'yes': 0.88, 'no': 1}, 'noBreakfast': {'price': 100, 'yes': 0.93, 'no': 1}}
    };

    if (days < 1) {
        console.log("Days must be positive number!")
    } else if (city in prices && pack in prices[city]) {
        let price = (prices[city][pack]['price'] * prices[city][pack][vip]) * days;
        console.log(`The price is ${price.toFixed(2)}lv! Have a nice time!`);
    } else {
        console.log('Invalid input!');
    }
}


travelAgency(['Borovets', 'noEquipment', 'yes', '6']);  // Expected Output:
// The price is 456.00lv! Have a nice time!

travelAgency(['Bansko', 'withEquipment', 'no', '2']);  // Expected Output:
// The price is 200.00lv! Have a nice time!

travelAgency(['Varna', 'withBreakfast', 'yes', '5']);  // Expected Output:
// The price is 572.00lv! Have a nice time!

travelAgency(['Burgas', 'noBreakfast', 'no', '5']);  // Expected Output:
// The price is 400.00lv! Have a nice time!
