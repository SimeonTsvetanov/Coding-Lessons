function transportPrice(...input) {
    let distance = Number(input.shift());
    let period = input.shift();

    if (distance >= 100) {
        // Then we can take the train and drink beer next to ugly old gipsy man singing pirate chalga songs :D
        console.log((distance * 0.06).toFixed(2));
    } else if(distance >= 20) {
        // Taking the bus then, enough chalga for one life :D
        console.log((distance * 0.09).toFixed(2));
    } else {
        // There is no else ... we broke as f***, WE WALK. Don't give me this taxi shit :D
        if (period === "day") {
            console.log(((distance * 0.79) + 0.70).toFixed(2));
        } else if (period === "night") {
            console.log(((distance * 0.90) + 0.70).toFixed(2));
        }
    }
}

transportPrice(['5', 'day']);  // Expected Output: 4.65
transportPrice(['7', 'night']);  // Expected Output: 7.00
transportPrice(['25', 'day']);  // Expected Output: 2.25
transportPrice(['180', 'night']);  // Expected Output: 10.80
