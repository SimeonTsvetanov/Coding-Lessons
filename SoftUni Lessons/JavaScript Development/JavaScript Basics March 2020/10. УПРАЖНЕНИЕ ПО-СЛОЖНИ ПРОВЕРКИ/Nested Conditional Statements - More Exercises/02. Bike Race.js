// Short link: https://bit.ly/2JhgeBP

function bikeRace(input) {
    let countJuniors = Number(input.shift());
    let countSeniors = Number(input.shift());
    let traceType = input.shift();

    let prices = {
        "trail": [5.5, 7],
        "cross-country": [8, 9.5],
        "downhill": [12.25, 13.75],
        "road": [20, 21.5]
    };

    let price = (prices[traceType][0] * countJuniors) + (prices[traceType][1] * countSeniors);

    if (traceType == "cross-country" && countJuniors + countSeniors >= 50) {
        price *= 0.75;
    }

    console.log(`${(price * 0.95).toFixed(2)}`);
}

bikeRace(['10', '20', 'trail']);  // Expected Output: 185.25
bikeRace(['20', '25', 'cross-country']);  // Expected Output: 377.63
bikeRace(['30', '25', 'cross-country']);  // Expected Output: 340.22
bikeRace(['10', '10', 'downhill']);  // Expected Output: 247.00
bikeRace(['3', '40', 'road']);  // Expected Output: 874.00
