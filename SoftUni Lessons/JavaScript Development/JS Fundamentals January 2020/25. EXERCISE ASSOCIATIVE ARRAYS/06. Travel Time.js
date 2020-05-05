function travelTime(input) {
    // Mask - This task takes more time to figure the f**** arrows in the print than the
    // whole logic... !
    let countries = {};

    input.forEach(data => {
        let [country, city, price] = data.split(' > ');
        if (!countries.hasOwnProperty(country)) {
            // New Country:
            countries[country] = {}
            countries[country][city] = Number(price);
        } else {
            // We have the Country already:
            if (!countries[country].hasOwnProperty(city)) {
                // New City
                countries[country][city] = Number(price);
            } else {
                // We have the city already:
                if (price < countries[country][city]) {
                    countries[country][city] = price;
                }
            }
        }
    })

    for (let country of Object.keys(countries).sort((a, b) => a.localeCompare(b))) {
        let result = `${country} -> `;
        for (let city of Object.keys(countries[country]).sort((a, b) =>
            countries[country][a] - countries[country][b])) {
            result += `${city} -> ${countries[country][city]} `;
        }
        console.log(result);
    }
}

travelTime([
        "Bulgaria > Sofia > 500",
        "Bulgaria > Sopot > 800",
        "France > Paris > 2000",
        "Albania > Tirana > 1000",
        "Bulgaria > Sofia > 200"
    ]);
// Should return:
// Albania -> Tirana -> 1000
// Bulgaria -> Sofia -> 200 Sopot -> 800
// France -> Paris -> 2000
