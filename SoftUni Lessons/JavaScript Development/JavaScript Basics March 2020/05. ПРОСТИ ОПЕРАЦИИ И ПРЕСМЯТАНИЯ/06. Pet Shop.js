function petShop(input) {
    let ownDogs = Number(input.shift());
    let otherAnimals = Number(input.shift());
    let price = (2.50 * ownDogs) + (4 * otherAnimals);
    let message = `${price.toFixed(2)} lv.`;
    console.log(message);
}

petShop(["5", "4"]);
petShop(["13", "9"]);
