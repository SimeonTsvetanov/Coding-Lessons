function mask(distance, passengers, price) {
    // Mask
    let neededFuel = ((distance / 100) * 7) + passengers * 0.100;
    let money = neededFuel * price;
    console.log(`Needed money for that trip is ${money}lv.`)
}

mask(260, 9, 2.49);  // Should return:
// Needed money for that trip is 47.559lv.

mask(90, 14, 2.88);  // Should return:
// Needed money for that trip is 22.176lv.
