function summerOutfit(input) {
    let temperature = Number(input.shift());
    let period = input.shift();

    // Shit is getting out of control This is list inside a dict inside a dict :D
    let clothes = {
        'from10to18': 
            {'Morning': ['Sweatshirt', 'Sneakers'], 'Afternoon': ['Shirt', 'Moccasins'], 'Evening': ['Shirt', 'Moccasins']},
        'from18to25': 
            {'Morning': ['Shirt', 'Moccasins'], 'Afternoon': ['T-Shirt', 'Sandals'], 'Evening': ['Shirt', 'Moccasins']},
        'above25': 
            {'Morning': ['T-Shirt', 'Sandals'], 'Afternoon': ['Swim Suit', 'Barefoot'], 'Evening': ['Shirt', 'Moccasins']}
    };

    let outfit = '';
    let shoes = '';

    if (temperature >= 10 && temperature <= 18) {
        outfit = clothes["from10to18"][period][0];
        shoes = clothes["from10to18"][period][1];
    } else if (temperature > 18 && temperature <= 24) {
        outfit = clothes["from18to25"][period][0];
        shoes = clothes["from18to25"][period][1];
    } else {
        outfit = clothes["above25"][period][0];
        shoes = clothes["above25"][period][1];
    }

    console.log(`It's ${temperature} degrees, get your ${outfit} and ${shoes}.`);
}

summerOutfit(['16', 'Morning']);
// Expected Putput: It's 16 degrees, get your Sweatshirt and Sneakers.

summerOutfit(['22', 'Afternoon']);
// Expected Putput: It's 22 degrees, get your T-Shirt and Sandals.

summerOutfit(['28', 'Evening']);
// Expected Putput: It's 28 degrees, get your Shirt and Moccasins.
