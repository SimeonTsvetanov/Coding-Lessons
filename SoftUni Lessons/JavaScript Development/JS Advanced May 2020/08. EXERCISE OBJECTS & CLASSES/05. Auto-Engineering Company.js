function autoEngineeringCompany(input) {
    // Mask - https://git.io/Jfre9
    let cars = {};

    input.map(data => {
        let [make, model, count] = data.split(' | ');
        count = +count;
        !cars.hasOwnProperty(make) ? cars[make] = {} : 'pass';
        cars[make].hasOwnProperty(model) ? cars[make][model] += count : cars[make][model] = count;
    });

    for (let [make, models] of Object.entries(cars)) {
        console.log(make);
        for (let [model, count] of Object.entries(models)) {
            console.log(`###${model} -> ${count}`);
        }
    }
}

autoEngineeringCompany([
    'Audi | Q7 | 1000',
    'Audi | Q6 | 100',
    'BMW | X5 | 1000',
    'BMW | X6 | 100',
    'Citroen | C4 | 123',
    'Volga | GAZ-24 | 1000000',
    'Lada | Niva | 1000000',
    'Lada | Jigula | 1000000',
    'Citroen | C4 | 22',
    'Citroen | C5 | 10']
);  // Should return:
// Audi
// ###Q7 -> 1000
// ###Q6 -> 100
// BMW
// ###X5 -> 1000
// ###X6 -> 100
// Citroen
// ###C4 -> 145
// ###C5 -> 10
// Volga
// ###GAZ-24 -> 1000000
// Lada
// ###Niva -> 1000000
// ###Jigula -> 1000000
