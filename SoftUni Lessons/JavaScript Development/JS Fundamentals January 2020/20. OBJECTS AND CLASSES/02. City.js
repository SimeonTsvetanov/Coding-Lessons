function solveCity(name, area, population, country, postcode) {
    // Mask
    let city = {
        name: name,
        area: area,
        population: population,
        country: country,
        postCode: postcode,
    };

    for (let cityKey in city) {
        console.log(`${cityKey} -> ${city[cityKey]}`);
    }
}

solveCity("Sofia"," 492", "1238438", "Bulgaria", "1000");
// Should return:
// name -> Sofia
// area -> 492
// population -> 1238438
// country -> Bulgaria
// postCode -> 1000
