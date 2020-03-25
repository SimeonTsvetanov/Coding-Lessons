function easterGuests(params) {
    let countPeople = Number(params.shift());
    let budget = Number(params.shift());

    let countEasterBreads = Math.ceil(countPeople / 3);
    let countEggs = countPeople * 2;

    let price = (countEasterBreads * 4) + (countEggs * 0.45);

    if (budget >= price) {
        console.log(`Lyubo bought ${countEasterBreads} Easter bread and ${countEggs} eggs.`);
        console.log(`He has ${(budget - price).toFixed(2)} lv. left.`)
    } else {
        console.log(`Lyubo doesn't have enough money.`);
        console.log(`He needs ${(price - budget).toFixed(2)} lv. more.`);
    }
}

easterGuests(['10', '35']);  // Expected Output:
// Lyubo bought 4 Easter bread and 20 eggs.
// He has 10.00 lv. left.

easterGuests(['9', '12']);  // Expected Output:
// Lyubo doesn't have enough money.
// He needs 8.10 lv. more.
