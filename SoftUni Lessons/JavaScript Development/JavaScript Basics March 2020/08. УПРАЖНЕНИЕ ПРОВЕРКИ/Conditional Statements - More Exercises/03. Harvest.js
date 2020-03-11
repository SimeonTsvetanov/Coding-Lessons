function harvest(input) {
    let sizeGargen = Number(input.shift());
    let grapesFor1sqare = Number(input.shift());
    let neededLiters = Number(input.shift());
    let countWorkers = Number(input.shift());

    let harvestArea = sizeGargen * 0.4;
    let grapesForHarvestedArea = harvestArea * grapesFor1sqare;
    let wine = grapesForHarvestedArea / 2.5;

    if (wine < neededLiters) {
        console.log(`It will be a tough winter! More ${Math.floor(neededLiters - wine)} liters wine needed.`);
    } else {
        console.log(`Good harvest this year! Total wine: ${Math.floor(wine)} liters.`);
        console.log(`${Math.ceil(wine - neededLiters)} liters left -> ${Math.ceil((wine - neededLiters) / countWorkers)} liters per person.`);
    }
}

harvest(['650', '2', '175', '3']);
// Expected output:
// Good harvest this year! Total wine: 208 liters.
// 33 liters left -> 11 liters per person.

harvest(['1020', '1.5', '425', '4']);
// Expected output:
// It will be a tough winter! More 180 liters wine needed.
