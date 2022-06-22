function travelTime (data) {
    // MasK
    function sortCountries(obj) {
        let sortedKVP = Array.from(Object.entries(obj)).sort((a, b) => {
            // Example Sort buy value (NUMBER) the smallest FIRST
            return a[0].localeCompare(b[0]) || 'if you want a second condition';
        });
        let sortedObject = {}
        for (let i = 0; i < sortedKVP.length; i ++) {
            sortedObject[sortedKVP[i][0]] = sortedKVP[i][1]
        }
        return sortedObject;
    }

    function sortCities(obj) {
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

    let countries = {};

    data.forEach(entry => {
        let country = entry.split(' > ')[0];
        let city = entry.split(' > ')[1];
        let cost = +entry.split(' > ')[2];

        if (!countries.hasOwnProperty(country)) {
            countries[country] = {}
            countries[country][city] = cost
        } else {
            if (!countries[country].hasOwnProperty(city)) {
                countries[country][city] = cost;
            } else {
                countries[country][city] = Math.min(cost, countries[country][city]);
            }
        }
    });

    countries = sortCountries(countries);

    for (let [country, cities] of Object.entries(countries)) {
        let result = '';
        cities = sortCities(cities);
        result += `${country} -> `;
        for (let [city, price] of Object.entries(cities)) {
            result += `${city} -> ${price} `
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
    ]
);

// Albania -> Tirana -> 1000
// Bulgaria -> Sofia -> 200 Sopot -> 800
// France -> Paris -> 2000

console.log();

travelTime([
        'Bulgaria > Sofia > 25000',
        'Bulgaria > Sofia > 25000',
        'Kalimdor > Orgrimar > 25000',
        'Albania > Tirana > 25000',
        'Bulgaria > Varna > 25010',
        'Bulgaria > Lukovit > 10'
    ]
);

// Albania -> Tirana -> 25000
// Bulgaria -> Lukovit -> 10 Sofia -> 25000 Varna -> 25010
// Kalimdor -> Orgrimar -> 25000
