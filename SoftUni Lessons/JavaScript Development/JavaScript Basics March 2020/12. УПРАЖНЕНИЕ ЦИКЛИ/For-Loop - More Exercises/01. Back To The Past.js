function backToThePast(input) {
    // Mask
    let money = Number(input.shift());
    let yearAim = input.shift();

    for (let year = 1800; year <= yearAim; year += 1) {
        if (year % 2 == 0) {
            money -= 12000;
        } else if (year % 2 != 0) {
            money -= (12000 + (50 * (year - 1800 + 18)));
        }
    }

    if (money >= 0) {
        console.log(`Yes! He will live a carefree life and will have ${money.toFixed(2)} dollars left.`);
    } else {
        console.log(`He will need ${Math.abs(money).toFixed(2)} dollars to survive.`);
    }
}

backToThePast([50000, 1802]);  // Should return:
// Yes! He will live a carefree life and will have 13050.00 dollars left.

backToThePast([100000.15, 1808]);  // Should return:
// He will need 12399.85 dollars to survive.