function dungeonDark (commands) {
    // MasK
    commands = commands[0].split('|');
    let health = 100;
    let coins = 0;
    let room = 0;
    let dead = false;

    for (const commandAndAmount of commands) {
        room ++;
        let command = commandAndAmount.split(' ')[0];
        let amount = Number(commandAndAmount.split(' ')[1]);

        if (command === 'potion') {
            // Drugs !!!
            amount + health > 100
                ? amount = amount - (health + amount - 100): 'asd';
            health += amount;
            console.log(`You healed for ${amount} hp.`);
            console.log(`Current health: ${health} hp.`);
        } else if (command === 'chest') {
            // Found Money
            coins += amount;
            console.log(`You found ${amount} coins.`);
        } else {
            // It's time for Fight:
            health -= amount;
            if (health > 0) {
                // Win
                console.log(`You slayed ${command}.`);
            } else {
                // Loose
                console.log(`You died! Killed by ${command}.`);
                console.log(`Best room: ${room}`);
                dead = true;
                break;
            }
        }
    }

    if (!dead) {
        console.log("You've made it!");
        console.log(`Coins: ${coins}`);
        console.log(`Health: ${health}`);
    }
}

dungeonDark(["rat 10|bat 20|potion 10|rat 10|chest 100|boss 70|chest 1000"]);
console.log('--------------------------------------------------------------');
dungeonDark(["cat 10|potion 30|orc 10|chest 10|snake 25|chest 110"]);