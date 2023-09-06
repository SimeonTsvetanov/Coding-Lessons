function mask (params) {
    // MASK
    let countries = {};

    params.forEach(x => {
        let country = x.split(' > ')[0];
        let city = x.split(' > ')[1];
        let price = Number(x.split(' > ')[2]);

        if (!(country in countries)) {
            countries[country] = {}
            countries[country][city] = price;
        } else if (country in countries) {
            if (!(city in countries[country])) {
                countries[country][city] = price;
            } else {
                countries[country][city] = Math.min(countries[country][city], price);
            }
        }
    });

    let sorted =Object.keys(countries).sort((a, b) => a.localeCompare(b));
    sorted.forEach(country => {
        let result = `${country} -> `;
        // const sorted = Object.entries(countries[country]).sort((x, y) => x[1] - y[1])
        for (let [town, price] of Object.entries(countries[country]).sort((a, b) => {return a[1] - b[1]})) {
            result += `${town} -> ${price} `;
        }
        console.log(result);
    });
}

mask([
"Bulgaria > Sofia > 500",
"Bulgaria > Sopot > 800",
"France > Paris > 2000",
"Albania > Tirana > 1000",
"Bulgaria > Sofia > 200"
]);
// Albania -> Tirana -> 1000
// Bulgaria -> Sofia -> 200 Sopot -> 800
// France -> Paris -> 2000

console.log('-------------------------------------');

mask([
'Bulgaria > Sofia > 25000',
'Bulgaria > Sofia > 25000',
'Kalimdor > Orgrimar > 25000',
'Albania > Tirana > 25000',
'Bulgaria > Varna > 25010',
'Bulgaria > Lukovit > 10'
]
);
// Albania -> Tirana -> 25000
// Bulgaria -> Lukovit -> 10 Sofia ->
// 25000 Varna -> 25010
// Kalimdor -> Orgrimar -> 25000

console.log('-------------------------------------');

mask([
'Bulgaria > Sofia > 25000',
'aaa > Sofia > 1',
'aa > Orgrimar > 0',
'Albania > Tirana > 25000',
'zz > Aarna > 25010',
'Bulgaria > Lukovit > 10'
]);
// aa -> Orgrimar -> 0
// aaa -> Sofia -> 1
// Albania -> Tirana -> 25000
// Bulgaria -> Lukovit -> 10 Sofia -> 25000
// zz -> Aarna -> 25010