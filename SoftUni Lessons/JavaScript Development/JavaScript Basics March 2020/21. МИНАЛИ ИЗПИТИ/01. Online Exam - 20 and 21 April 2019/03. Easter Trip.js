function easterTrip(params) {
    let country = params.shift();
    let period = params.shift();
    let nights = Number(params.shift());

    let prices = {
        'France': {'21-23': 30, '24-27': 35, '28-31': 40},
        'Italy': {'21-23': 28, '24-27': 32, '28-31': 39},
        'Germany': {'21-23': 32, '24-27': 37, '28-31': 43}
    };

    let price = prices[country][period] * nights;

    console.log(`Easter trip to ${country} : ${price.toFixed(2)} leva.`);
}

easterTrip(['Germany', '24-27', '5']);  // Expected output:
// Easter trip to Germany : 185.00 leva.

easterTrip(['Italy', '21-23', '7']);  // Expected output:
// Easter trip to Italy : 196.00 leva.

easterTrip(['France', '28-31', '8']);  // Expected output:
// Easter trip to France : 320.00 leva.