function fuelTank(input) {
    let fueltype = input.shift();
    let leftFuel = Number(input.shift());

    // Being too lazy I've used a few cheats here: 
    // [list](to find them quick) and the toLowerCase() Method for the print :)
    
    if (["Diesel", "Gasoline", "Gas"].includes(fueltype)) {
        if (leftFuel >= 25) {
            console.log(`You have enough ${fueltype.toLowerCase()}.`);
        } else {
            console.log(`Fill your tank with ${fueltype.toLowerCase()}!`);
        }
    } else {
        console.log('Invalid fuel!');
    }
}

fuelTank(['Diesel', '10']);  // Expectedoutput: Fill your tank with diesel!
fuelTank(['Gasoline', '40']);  // Expectedoutput: You have enough gasoline.
fuelTank(['Gas', '25']);  // Expectedoutput: You have enough gas.
fuelTank(['Kerosene', '25']);  // Expectedoutput: Invalid fuel!
