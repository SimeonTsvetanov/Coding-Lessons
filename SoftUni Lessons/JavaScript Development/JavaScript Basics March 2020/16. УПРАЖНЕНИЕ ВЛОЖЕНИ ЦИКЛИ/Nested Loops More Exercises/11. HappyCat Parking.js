function happyCatParking(input) {
    // Mask
    let days = Number(input.shift());
    let hours = Number(input.shift());

    let total = 0;

    for (let day = 1; day <= days; day += 1) {
        let price = 0;
        for (let hour = 1; hour <= hours; hour += 1) {
            if ((day % 2 == 0) && hour % 2 != 0) {price += 2.5;}
            else if ((day % 2 != 0) && (hour % 2 == 0)) {price += 1.25;}
            else {price += 1;}
        }
        total += price;
        console.log(`Day: ${day} - ${price.toFixed(2)} leva`);
    }

    console.log(`Total: ${total.toFixed(2)} leva`);
}

happyCatParking([2, 5]);  // Should return:
// Day: 1 - 5.50 leva
// Day: 2 - 9.50 leva
// Total: 15.00 leva

happyCatParking([5, 2]);  // Should return:
// Day: 1 - 2.25 leva
// Day: 2 - 3.50 leva
// Day: 3 - 2.25 leva
// Day: 4 - 3.50 leva
// Day: 5 - 2.25 leva
// Total: 13.75 leva
