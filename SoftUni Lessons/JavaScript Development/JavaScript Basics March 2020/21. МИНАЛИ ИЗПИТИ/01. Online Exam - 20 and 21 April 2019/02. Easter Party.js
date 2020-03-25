function easterParty(params) {
    let countGuests = Number(params.shift());
    let priceOnePerson = Number(params.shift());
    let budget = Number(params.shift());

    if (countGuests >= 10 && countGuests <= 15) {
        priceOnePerson *= 0.85;
    } else if (countGuests > 15 && countGuests <= 20) {
        priceOnePerson *= 0.8;
    } else if (countGuests > 20) {
        priceOnePerson *= 0.75;
    }

    let total = (priceOnePerson * countGuests) + (budget * 0.1);

    if (budget >= total) {
        console.log(`It is party time! ${(budget - total).toFixed(2)} leva left.`);
    } else {
        console.log(`No party! ${(total - budget).toFixed(2)} leva needed.`);
    }
}


easterParty(['18', '30', '450']);  // Expected Output: No party! 27.00 leva needed.
easterParty(['8', '25', '340']);  // Expected Output: It is party time! 106.00 leva left.
easterParty(['24', '35', '550']);  // Expected Output: No party! 135.00 leva needed.