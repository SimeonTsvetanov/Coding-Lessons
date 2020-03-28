function skiTrip(...input) {
    let nights = Number(input.shift()) - 1;  // as we are looking for nights which are days -=1
    let accommodation = input.shift();
    let evaluation = input.shift();
    
    // How it works:
    // "type of acc.": [(base day price), (dissc. < 10 days), (discount 10 <= days <= 15), (discount days > 15)] 
    let rates = {
        "room for one person": [18, 1, 1, 1],
        "apartment": [25, 0.7, 0.65, 0.5],
        "president apartment": [35, 0.9, 0.85, 0.8]
    };

    let price = 0;

    if (nights < 10) {
        // How it works ... nights * base day price * discount 
        price = nights * rates[accommodation][0] * rates[accommodation][1];
    } else if (nights >= 10 && nights <= 15){
        price = nights * rates[accommodation][0] * rates[accommodation][2];
    } else if (nights > 15) {
        price = nights * rates[accommodation][0] * rates[accommodation][3];
    }

    // Used switch just for the sake of it :D
    switch(evaluation) {
        case "positive":
            price += price * 0.25;
            break
        case "negative":
            price -= price * 0.1;
    }

    console.log(price.toFixed(2));
}


skiTrip(['14', 'apartment', 'positive']);  // Expected Output: 264.06
skiTrip(['30', 'president apartment', 'negative']);  // Expected Output: 730.80
skiTrip(['12', 'room for one person', 'positive']);  // Expected Output: 247.50
skiTrip(['2', 'apartment', 'positive']);  // Expected Output: 21.88