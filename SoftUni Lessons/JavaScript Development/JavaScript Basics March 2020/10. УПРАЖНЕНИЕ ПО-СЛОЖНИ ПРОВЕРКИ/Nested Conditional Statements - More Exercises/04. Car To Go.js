function carToGO(...input) {
    let budget = Number(input.shift());
    let season = input.shift();  // Summer or Winter
    
    let classCar = undefined;
    let typeCar = undefined;
    let priceCar = undefined;

    if (budget <= 100) {
        classCar = "Economy class";
        switch (season) {
            case "Summer":
                typeCar = "Cabrio";
                priceCar = budget * 0.35;
                break;
            case "Winter":
                typeCar = "Jeep";
                priceCar = budget * 0.65;
        }
    } else if (budget > 100 && budget <= 500) {
        classCar = "Compact class";
        switch (season) {
            case "Summer":
                typeCar = "Cabrio";
                priceCar = budget * 0.45;
                break;
            case "Winter":
                typeCar = "Jeep";
                priceCar = budget * 0.80;
        }
    } else {
        classCar = "Luxury class";
        typeCar = "Jeep";
        priceCar = budget * 0.90;
    }

    console.log(classCar);
    console.log(`${typeCar} - ${priceCar.toFixed(2)}`);
}


carToGO(['450', 'Summer']); // Expected Output:
// Compact class
// Cabrio - 202.50

carToGO(['450', 'Winter']); // Expected Output:
// Compact class
// Jeep - 360.00

carToGO(['1010', 'Summer']); // Expected Output:
// Luxury class
// Jeep - 909.00

carToGO(['99.99', 'Summer']); // Expected Output:
// Economy class
// Cabrio - 35.00

carToGO(['1010', 'Winter']); // Expected Output:
// Luxury class
// Jeep - 909.00

carToGO(['70.50', 'Winter']); // Expected Output:
// Economy class
// Jeep - 45.83
