// Not included in final score
function fishTank(input) {
    let width = input.shift();
    let length = input.shift();
    let height = input.shift();
    let procentage = input.shift();

    let neededWater = (((width * length * height) / 1000) * (1 - (procentage * 0.01))).toFixed(3);
    console.log(neededWater);
}

fishTank(["85", "75", "47", "17"]);
fishTank(["105", "77", "89", "18.5"]);