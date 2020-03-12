function smallShop(input) {
    let product = input.shift();
    let city = input.shift();
    let volume = Number(input.shift());

    // Yeah, nested Dictionary... but was I really supposed to write 50 lines of ugly if... else bul***its.
    let prices = {
        "Sofia": {"coffee": 0.50, "water": 0.80, "beer": 1.20, "sweets": 1.45, "peanuts": 1.60},
        "Plovdiv": {"coffee": 0.40, "water": 0.70, "beer": 1.15, "sweets": 1.30, "peanuts": 1.50},
        "Varna": {"coffee": 0.45, "water": 0.70, "beer": 1.10, "sweets": 1.35, "peanuts": 1.55}
    };
    
    let price = prices[city][product] * volume;
    console.log(price);
}

smallShop(["coffee", "Varna", "2"]);  // Expected Output: 0.9
smallShop(["peanuts", "Plovdiv", "1"]);  // Expected Output: 0.9
smallShop(["beer", "Sofia", "6"]);  // Expected Output: 0.9
smallShop(["water", "Plovdiv", "3"]);  // Expected Output: 0.9
smallShop(["sweets", "Sofia", "2.23"]);  // Expected Output: 0.9
