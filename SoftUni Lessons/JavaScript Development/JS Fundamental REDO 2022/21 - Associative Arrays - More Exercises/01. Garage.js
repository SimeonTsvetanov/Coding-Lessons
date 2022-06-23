function garage (data) {
    // MasK
    let garages = {};

    data.forEach(entry => {
        // Sort the Input:
        entry = entry.split(' - ');
        let newGarage = +entry.shift();
        let carData = entry.shift().split(', ').map(a => {return a = a.split(': ')});
        let car = {};
        for (let i = 0; i < carData.length; i ++) { car[carData[i][0]] = carData[i][1] }

        // Fill the input:
        garages.hasOwnProperty(newGarage) ? garages[newGarage].push(car) : garages[newGarage] = [car];
    });

    // Print the desired output:
    for (let [garageNumber, cars] of Object.entries(garages)) {
        console.log(`Garage № ${garageNumber}`);
        cars.forEach(car => {
            let details = Array.from(Object.entries(car)).map(a => {return `${a[0]} - ${a[1]}`});
            console.log(`--- ${details.join(', ')}`);
        });
    }
}

garage(['1 - color: blue, fuel type: diesel', '1 - color: red, manufacture: Audi', '2 - fuel type: petrol', '4 - color: dark blue, fuel type: diesel, manufacture: Fiat']);
// Garage № 1
// --- color - blue, fuel type - diesel
// --- color - red, manufacture - Audi
// Garage № 2
// --- fuel type - petrol
// Garage № 4
// --- color - dark blue, fuel type - diesel, manufacture - Fiat

console.log();

garage(['1 - color: green, fuel type: petrol',
    '1 - color: dark red, manufacture: WV',
    '2 - fuel type: diesel',
    '3 - color: dark blue, fuel type: petrol']
);
// Garage № 1
// --- color - green, fuel type - petrol
// --- color - dark red, manufacture - WV
// Garage № 2
// --- fuel type - diesel
// Garage № 3
// --- color - dark blue, fuel type - petrol


function sortObject(obj) {
    let sortedKVP = Array.from(Object.entries(obj)).sort((a, b) => {
        // Example Sort buy value (NUMBER) the smallest FIRST
        return a[1] - b[1] || 'if you want a second condition';
    });
    let sortedObject = {}
    for (let i = 0; i < sortedKVP.length; i ++) {
        sortedObject[sortedKVP[i][0]] = sortedKVP[i][1]
    }
    return sortedObject;
}