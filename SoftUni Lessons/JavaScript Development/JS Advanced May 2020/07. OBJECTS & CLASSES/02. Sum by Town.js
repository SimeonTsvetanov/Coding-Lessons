function sumByTowns(input) {
    // Mask
    let towns = {};

    while (input.length > 0) {
        let city = input.shift();
        let value = Number(input.shift());
        towns.hasOwnProperty(city) ? towns[city] += value : towns[city] = value;
    }
    console.log(JSON.stringify(towns));
}

sumByTowns(['Sofia','20','Varna','3','Sofia','5','Varna','4']);
// Should return: {"Sofia":25,"Varna":7}

sumByTowns(['Sofia','20','Varna','3','sofia','5','varna','4']);
// Should return: {"Sofia":20,"Varna":3,"sofia":5,"varna":4}