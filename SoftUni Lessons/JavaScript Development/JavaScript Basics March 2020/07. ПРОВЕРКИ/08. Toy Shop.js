//  Not included in final score

function toyShop(input) {
    
    // This Dictionary Object is not needed.... But I wanted to flex a bit :D
    let toy_prices = {
        "puzzel": 2.60,
        "speakingDoll": 3,
        "teddyBear": 4.10,
        "minion": 8.20,
        "truck": 2
    };

    let excursionPrice = Number(input.shift());
    
    let puzzelsCount = Number(input.shift());
    let speakingDollsCount = Number(input.shift());
    let teddyBearsCount = Number(input.shift());
    let minionsCount = Number(input.shift());
    let trucksCount = Number(input.shift());

    let totalCount = puzzelsCount + speakingDollsCount + teddyBearsCount + minionsCount + trucksCount;

    let puzzelsPrice = puzzelsCount * toy_prices["puzzel"];
    let speakingDollsPrice = speakingDollsCount * toy_prices["speakingDoll"];
    let teddyBearsPrice = teddyBearsCount * toy_prices["teddyBear"];
    let minionsPrice = minionsCount * toy_prices["minion"];
    let trucksPrice = trucksCount * toy_prices["truck"];

    let totalPrice = (puzzelsPrice + speakingDollsPrice + teddyBearsPrice + minionsPrice + trucksPrice) * 0.9

    if (totalCount >= 50) {
        totalPrice *= 0.75
    }
    
    if (totalPrice >= excursionPrice) {
        console.log(`Yes! ${(totalPrice - excursionPrice).toFixed(2)} lv left.`)
    }
    else {
        console.log(`Not enough money! ${(excursionPrice - totalPrice).toFixed(2)} lv needed.`)
    }
}

toyShop([40.8, 20, 25, 30, 50, 10])  // Expected output:  Yes! 418.20 lv left.
toyShop([320, 8, 2, 5, 5, 1])  // Expected output:  Not enough money! 238.73 lv needed.
