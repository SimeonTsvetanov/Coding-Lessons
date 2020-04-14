function rounding(number, precision) {
    // Mask
    if (precision > 15) {
        precision = 15;
    }
    console.log(parseFloat(number.toFixed(precision)));
}

rounding(3.1415926535897932384626433832795, 2);  // Should return: 3.14

rounding(10.5, 3);  // Should return: 10.5
