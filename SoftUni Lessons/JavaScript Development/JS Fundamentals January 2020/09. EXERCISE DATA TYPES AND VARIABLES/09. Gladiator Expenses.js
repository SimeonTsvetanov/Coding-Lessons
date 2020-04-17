function gladiatorExpenses(lostFightsCount, helmetPrice, swordPrice, shieldPrice, armorPrice) {
    // Mask
    let expenses = 0;
    let brokenShieldCounter = 0;

    for (let fight = 1; fight <= lostFightsCount; fight += 1) {
        let helmet = false;
        let sword = false;

        if (fight % 2 === 0) {
            // Helmet is broken
            expenses += helmetPrice;
            helmet = true;
        }
        if (fight % 3 === 0) {
            // Sword is broken
            expenses += swordPrice;
            sword = true;
        }
        if (helmet && sword) {
            // Shield is broken
            expenses += shieldPrice;
            brokenShieldCounter += 1;
            helmet = false; sword = false;
        }
        if (brokenShieldCounter === 2) {
            // Armor is broken
            expenses += armorPrice;
            brokenShieldCounter = 0
        }

    }
    console.log(`Gladiator expenses: ${expenses.toFixed(2)} aureus`);
}

gladiatorExpenses(7, 2, 3, 4, 5);
// Should return: Gladiator expenses: 16.00 aureus

gladiatorExpenses(23, 12.50, 21.50, 40, 200);
// Should return: Gladiator expenses: 608.00 aureus