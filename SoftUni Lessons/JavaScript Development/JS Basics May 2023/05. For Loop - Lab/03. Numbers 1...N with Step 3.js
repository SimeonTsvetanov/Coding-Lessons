function numbersFromOneToNwithStep(params) {
    let step = 3;
    let range = Number(params.shift());
    for (let i = 1; i <= range; i += step) console.log(i);
}

