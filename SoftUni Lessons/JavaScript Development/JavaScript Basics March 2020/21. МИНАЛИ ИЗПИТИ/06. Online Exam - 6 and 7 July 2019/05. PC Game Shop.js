function pcGameShop(input) {
    // Mask
    // Fuck Games: Go learn to code!
    // Games in BED ONLY!
    games = {
        'Hearthstone': 0,
        'Fornite': 0,
        'Overwatch': 0,
        'Others': 0
    }

    let count = Number(input.shift());

    for (let game = 1; game <= count; game += 1) {
        let game = input.shift();
        if (game in games) {
            games[game] += 1;
        } else {
            games["Others"] += 1;
        }
    }

    console.log(`Hearthstone - ${(games['Hearthstone'] / count * 100).toFixed(2)}%`);
    console.log(`Fornite - ${(games['Fornite'] / count * 100).toFixed(2)}%`);
    console.log(`Overwatch - ${(games['Overwatch'] / count * 100).toFixed(2)}%`);
    console.log(`Others - ${(games['Others'] / count * 100).toFixed(2)}%`);
}

pcGameShop([4, 'Hearthstone', 'Fornite', 'Overwatch', 'Counter-Strike']);  
// Should return:
// Hearthstone - 25.00%
// Fornite - 25.00%
// Overwatch - 25.00%
// Others - 25.00%

pcGameShop([3, 'Hearthstone', 'Diablo 2', 'Star Craft 2']);  
// Should return:
// Hearthstone - 33.33%
// Fornite - 0.00%
// Overwatch - 0.00%
// Others - 66.67%
