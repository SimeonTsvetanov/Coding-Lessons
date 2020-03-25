function lemonadeStand(params) {
    let lemons = Number(params.shift());
    let sugar = Number(params.shift());
    let water = Number(params.shift());

    let glasses = Math.floor(((lemons * 980) + (water * 1000) + (0.3 * sugar)) / 150);
    let money = (glasses * 1.20).toFixed(2);

    console.log(`All cups sold: ${glasses}`);
    console.log(`Money earned: ${money}`);
}


lemonadeStand([5, 3.5, 5]);  // Expected output:
// All cups sold: 66
// Money earned: 79.20

lemonadeStand([250, 20, 100]);  // Expected output:
// All cups sold: 2300
// Money earned: 2760.00

lemonadeStand([85, 17.5, 35]);  // Expected output:
// All cups sold: 788
// Money earned: 945.60

