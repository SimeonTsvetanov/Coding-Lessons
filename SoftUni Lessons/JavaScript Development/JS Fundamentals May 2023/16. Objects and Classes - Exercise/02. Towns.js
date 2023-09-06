function mask (params) {
    // MASK
    let towns = [];

    params.forEach(param => {
        let name = param.split(' | ')[0];
        let lat = Number(param.split(' | ')[1]).toFixed(2);
        let long = Number(param.split(' | ')[2]).toFixed(2);
        towns.push({'town': name, 'latitude': lat, 'longitude': long});
    });

    towns.forEach(town => { console.log(town); });
}

mask(['Sofia | 42.696552 | 23.32601',
'Beijing | 39.913818 | 116.363625']);
// { town: 'Sofia', latitude: '42.70', longitude: '23.33' }
// { town: 'Beijing', latitude: '39.91', longitude: '116.36' }

console.log('-------------------------------------');

mask(['Plovdiv | 136.45 | 812.575']);
// { town: 'Plovdiv', latitude: '136.45', longitude: '812.58' }

