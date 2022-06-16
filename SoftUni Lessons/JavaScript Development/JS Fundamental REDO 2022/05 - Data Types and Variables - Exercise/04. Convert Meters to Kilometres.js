function metersToKilometers (...args) {
    // MasK
    let meters = args[0];   // meters
    let result = meters / 1000;
    console.log(result.toFixed(2));
}

metersToKilometers(1852);