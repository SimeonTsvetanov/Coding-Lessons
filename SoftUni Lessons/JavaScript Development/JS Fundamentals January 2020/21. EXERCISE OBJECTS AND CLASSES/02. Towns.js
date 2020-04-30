function towns(input) {
    // Mask

    input.map((data) => {
        let [name, latitude, longitude] = data.split(' | ');
        let city = {};
        city.town = name;
        city.latitude = (Number(latitude)).toFixed(2);
        city.longitude = (Number(longitude)).toFixed(2);

        console.log(city);
    });
}

towns(['Sofia | 42.696552 | 23.32601', 'Beijing | 39.913818 | 116.363625']);
// Should return:
// { town: 'Sofia', latitude: '42.70', longitude: '23.33' }
// { town: 'Beijing', latitude: '39.91', longitude: '116.36' }
