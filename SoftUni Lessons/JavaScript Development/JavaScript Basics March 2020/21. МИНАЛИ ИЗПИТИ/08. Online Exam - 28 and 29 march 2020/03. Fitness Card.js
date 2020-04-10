function fitnessCard(input) {
    // Mask
    let budget = Number(input.shift());
    let gender = input.shift();
    let age = Number(input.shift());
    let sport = input.shift();
    
    // Just before we continue:
    // Haveing different priced depending on the SEX:
    // is fuck**g SEXIST. You sick fuck.

    let prices = {
        'm': {'Gym': 42, 'Boxing': 41, 'Yoga': 45, 'Zumba': 34, 'Dances': 51, 'Pilates': 39},
        'f': {'Gym': 35, 'Boxing': 37, 'Yoga': 42, 'Zumba': 31, 'Dances': 53, 'Pilates': 37}
    };

    let price = prices[gender][sport];
    if (age <= 19) {price *= 0.8;}

    if (budget >= price) {
        console.log(`You purchased a 1 month pass for ${sport}.`);
    } else {
        console.log(`You don't have enough money! You need $${(price - budget).toFixed(2)} more.`);
    }
}

fitnessCard([50, 'm', 23, 'Gym']);  // Should return:
// You purchased a 1 month pass for Gym.

fitnessCard([20, 'f', 15, 'Yoga']);  // Should return:
// You don't have enough money! You need $13.60 more.