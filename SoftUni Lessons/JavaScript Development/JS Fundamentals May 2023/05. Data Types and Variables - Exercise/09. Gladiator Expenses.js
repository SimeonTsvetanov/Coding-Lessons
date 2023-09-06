function mask (lostFights, helmetPrice, swordPrice, shieldPrice, armorPrice) {
    // MASK
    let helmet = 0;
    let sword = 0;
    let shield = 0;
    let armor = 0;

    for (let fight = 1; fight <= lostFights; fight++) {
        if (fight % 2 === 0) { helmet += 1; }
        if (fight % 3 === 0) { sword += 1; }
        if (fight % 2 === 0 && fight % 3 === 0) {
            shield += 1;
            if (shield % 2 == 0) {armor += 1};
        }
    }

    let total = (helmet * helmetPrice) + (sword * swordPrice) + (shield * shieldPrice) + (armor * armorPrice);
    console.log(`Gladiator expenses: ${total.toFixed(2)} aureus`);
}

mask(7,
2,
3,
4,
5);
// Gladiator expenses: 16.00 aureus

mask(23,
12.50,
21.50,
40,
200
);
// Gladiator expenses: 608.00 aureus
