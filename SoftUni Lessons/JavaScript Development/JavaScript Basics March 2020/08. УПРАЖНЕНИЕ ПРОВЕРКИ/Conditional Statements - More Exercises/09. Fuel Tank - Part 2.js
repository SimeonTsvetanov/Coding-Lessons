function fuelTankTwo(...input) {
    let typeFuel = input.shift();
    let litersFuel = Number(input.shift());
    let clubCard = input.shift();

    // Using dict with array here, makes it just a tiny bit easier, yet so much fancier :F
    let fuelPrices = {
        // {Name: [price, discount]}
        "Gasoline": [2.22, 0.18],
        "Diesel": [2.33, 0.12],
        "Gas": [0.93, 0.08]
    };

    let price = litersFuel * fuelPrices[typeFuel][0];  // Told ya :D
    if (clubCard === "Yes") {
        price -= litersFuel * fuelPrices[typeFuel][1];  // Aint that beautiful...
    }
    if (litersFuel >= 20 && litersFuel <= 25) {
        price *= 0.92;  // That's how you remove 8% like a boss :D
    } else if(litersFuel > 25) {
        price *= 0.9  // or 10.
    }
    console.log(`${price.toFixed(2)} lv.`);
}

fuelTankTwo(['Gas', '30', 'Yes']);  // Expected Output: 22.95 lv.
fuelTankTwo(['Gasoline', '25', 'No']);  // Expected Output: 51.06 lv.
fuelTankTwo(['Diesel', '19', 'No']);  // Expected Output: 44.27 lv.
