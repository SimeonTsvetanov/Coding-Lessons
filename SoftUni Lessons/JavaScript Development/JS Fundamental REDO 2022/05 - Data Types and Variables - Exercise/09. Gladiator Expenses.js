function gladiatorExpenses(lostFights, helmetPrice, swordPrice, shieldPrice, armorPrice) {

    let helmetCount = 0;
    let swordCount = 0;
    let shieldCount = 0;
    let shieldTimesBroken = 0;
    let armorCount = 0;

    for (let i = 1; i <= lostFights; i++) {
        i % 2 === 0 ? helmetCount += 1 : 'pass';
        i % 3 === 0 ? swordCount += 1 : 'pass';
        if (i % 2 === 0 && i % 3 === 0) {
            shieldCount += 1;
            shieldTimesBroken += 1;
            if (shieldTimesBroken === 2) {
                armorCount += 1;
                shieldTimesBroken = 0;
            }
        }
    }

    let expenses = (helmetPrice * helmetCount) + (swordPrice * swordCount) + (shieldPrice * shieldCount) + (armorPrice * armorCount);
    console.log(`Gladiator expenses: ${expenses.toFixed(2)} aureus`);
}

gladiatorExpenses(7,
    2,
    3,
    4,
    5
);
