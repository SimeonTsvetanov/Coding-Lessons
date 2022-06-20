function towns (data) {
    // MasK
    let towns = [];

    data.forEach(city => {
        let name = city.split(' | ')[0];
        let lat = Number(city.split(' | ')[1]).toFixed(2);
        let long = Number(city.split(' | ')[2]).toFixed(2);

        let newTown = {
            town: name,
            latitude: lat,
            longitude: long,
        }
        towns.push(newTown);
    });

    towns.forEach(town => {
        console.log(town);
    });
}



towns(['Sofia | 42.696552 | 23.32601',
    'Beijing | 39.913818 | 116.363625']
);

// { town: 'Sofia', latitude: '42.70', longitude: '23.33' }
// { town: 'Beijing', latitude: '39.91', longitude: '116.36' }