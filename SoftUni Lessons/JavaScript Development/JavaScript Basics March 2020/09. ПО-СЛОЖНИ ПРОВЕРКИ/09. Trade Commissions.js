function tradeCommissitons(input) {
    let city = input.shift();
    let volume = Number(input.shift());

    // I feel like Dict with lists is better :D
    let commissions = {
        'Sofia': [0.05, 0.07, 0.08, 0.12],
        'Varna': [0.045, 0.075, 0.1, 0.13],
        'Plovdiv': [0.055, 0.08, 0.12, 0.145]
    };

    if (['Sofia', 'Varna', 'Plovdiv'].includes(city) && volume >= 0) {
        if (volume >= 0 && volume <= 500) {
            console.log((commissions[city][0] * volume).toFixed(2));
        } else if (volume > 500 && volume <= 1000) {
            console.log((commissions[city][1] * volume).toFixed(2));
        } else if (volume > 1000 && volume <= 10000) {
            console.log((commissions[city][2] * volume).toFixed(2));
        } else if (volume > 10000) {
            console.log((commissions[city][3] * volume).toFixed(2));
        }
    } else {
        console.log('error');
    }
}

tradeCommissitons(['Sofia', '1500']);  //Expected Output: 120.00
tradeCommissitons(['Plovdiv', '499.99']);  //Expected Output: 120.00
tradeCommissitons(['Varna', '3874.50']);  //Expected Output: 120.00
tradeCommissitons(['Smolyan', '-50']);  //Expected Output: 120.00
