function townsToJson(input) {
    // Mask
    let [town, latitude, longitude]= input[0].split(' ').join('').split('|').filter(Boolean);

    let towns = [];
    for (let i = 1; i < input.length; i++) {
        let current = input[i].split('|').filter(Boolean);

        let town = current[0].trim();
        let latitude = Number(Number(current[1]).toFixed(2));
        let longitude = Number(Number(current[2]).toFixed(2));

        towns.push({Town: town, Latitude: latitude, Longitude: longitude});
    }
    console.log(JSON.stringify(towns));
}

townsToJson(['| Town | Latitude | Longitude |',
    '| Sofia | 42.696552 | 23.32601 |',
    '| Beijing | 39.913818 | 116.363625 |']);
// Should return:
// [{"Town":"Sofia",
//     "Latitude":42.7,
//     "Longitude":23.32
// },
//     {"Town":"Beijing",
//         "Latitude":39.91,
//         "Longitude":116.36
//     }]

townsToJson(['| Town | Latitude | Longitude |',
    '| Veliko Turnovo | 43.0757 | 25.6172 |',
    '| Monatevideo | 34.50 | 56.11 |']);
// Should return:
// [{"Town":"Veliko Turnovo",
//     "Latitude":43.08,
//     "Longitude":25.62
// },
//     {"Town":"Monatevideo",
//         "Latitude":34.5,
//         "Longitude":56.11
//     }]
