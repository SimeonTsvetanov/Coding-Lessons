function dungeonestDark(input) {
    // Mask
    let dungeons = input.shift().split('|');
    let health = 100;
    let coins = 0;
    let alive = true;

    for (let dungeon = 0; dungeon < dungeons.length; dungeon += 1) {
        let action = dungeons[dungeon].split(' ')[0];
        let value = Number(dungeons[dungeon].split(' ')[1]);

        if (action === 'potion') {
            // HEAL
            console.log(`You healed for ${value + health > 100 ? 100 - health : value} hp.`);
            value + health > 100 ? health = 100 : health += value;
            console.log(`Current health: ${health} hp.`);
        } else if (action === 'chest') {
            // GET MONEY
            coins += value;
            console.log(`You found ${value} coins.`);
        } else {
            // FIGHT
            health -= value; // get that damage.
            if (health > 0) {
                // WIN
                console.log(`You slayed ${action}.`);
            } else {
                // LOOSE
                console.log(`You died! Killed by ${action}.`);
                console.log(`Best room: ${dungeon + 1}`);
                alive = false;
                break;
            }
        }
    }

    if (alive) {
        console.log(`You've made it!`);
        console.log(`Coins: ${coins}`);
        console.log(`Health: ${health}`);
    }
}

dungeonestDark(['rat 10|bat 20|potion 10|rat 10|chest 100|boss 70|chest 1000']);  // Should return:
// You slayed rat.
// You slayed bat.
// You healed for 10 hp.
// Current health: 80 hp.
// You slayed rat.
// You found 100 coins.
// You died! Killed by boss.
// Best room: 6

dungeonestDark(['cat 10|potion 30|orc 10|chest 10|snake 25|chest 110']);  // Should return:
// You slayed cat.
// You healed for 10 hp.
// Current health: 100 hp.
// You slayed orc.
// You found 10 coins.
// You slayed snake.
// You found 110 coins.
// You've made it!
// Coins: 120
// Health: 65
