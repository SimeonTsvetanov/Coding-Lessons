function muOnline(input) {
    // Mask
    let health = 100;
    let bitCoins = 0;

    let rooms = input.shift().split('|');

    let dead = false;

    for (let room of rooms) {
        let command = room.split(' ')[0];
        let value = Number(room.split(' ')[1]);

        if (command === 'potion') {
            let bonus = health + value <= 100 ? value : 100 - health;
            health = Math.min(health + value, 100);  // So the health will be max 100.
            console.log(`You healed for ${bonus} hp.`);
            console.log(`Current health: ${health} hp.`);
        } else if (command === 'chest') {
            bitCoins += value;
            console.log(`You found ${value} bitcoins.`);
        } else {
            health -= value;
            if (health > 0) {
                console.log(`You slayed ${command}.`);
            } else {
                console.log(`You died! Killed by ${command}.`);
                console.log(`Best room: ${rooms.indexOf(room) + 1}`);
                dead = true;
                break;
            }
        }
    }

    if (!dead) {
        console.log(`You've made it!\nBitcoins: ${bitCoins}\nHealth: ${health}`);
    }
}

muOnline([ 'rat 10|bat 20|potion 10|rat 10|chest 100|boss 70|chest 1000' ]);
// Should return:
// You slayed rat.
// You slayed bat.
// You healed for 10 hp.
// Current health: 80 hp.
// You slayed rat.
// You found 100 bitcoins.
// You died! Killed by boss.
// Best room: 6

muOnline([ 'cat 10|potion 30|orc 10|chest 10|snake 25|chest 110' ]);
// Should return:
// You slayed cat.
// You healed for 10 hp.
// Current health: 100 hp.
// You slayed orc.
// You found 10 bitcoins.
// You slayed snake.
// You found 110 bitcoins.
// You've made it!
// Bitcoins: 120
// Health: 65
