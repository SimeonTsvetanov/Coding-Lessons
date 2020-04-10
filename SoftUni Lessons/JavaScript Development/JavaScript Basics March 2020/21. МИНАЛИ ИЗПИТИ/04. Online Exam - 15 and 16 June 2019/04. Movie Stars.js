function movieStars(input) {
    // Mask
    let budget = Number(input.shift());

    while ('ACTION or NO MORE MONEY') {
        let name = input.shift();
        if (name == 'ACTION') {
            console.log(`We are left with ${budget.toFixed(2)} leva.`);
            break;
        }

        if (name.length > 15) {
            budget -= budget * 0.2;
        } else {
            budget -= Number(input.shift());
        }
    
        if (budget < 0) {
            console.log(`We need ${Math.abs(budget).toFixed(2)} leva for our actors.`);
            break;
        }
    }
}

movieStars([90000, 'Christian Bale', 70000.50, 'Leonard DiCaprio', 'Kevin Spacey', 24000.99]); 
// Should return:
//  We need 8001.39 leva for our actors.

movieStars([170000, 'Ben Affleck', 40000.50, 'Zahari Baharov', 80000, 'Tom Hanks', 2000.99, 'ACTION']);  
// Should return:
// We are left with 47998.51 leva.