function mask (params) {
    // MASK
    let health = 100;
    let coins = 0;
    let rooms = params.shift().split('|');


    for (let i = 0; i < rooms.length; i++) {
        let room = rooms[i]
        let item_or_monster = room.split(' ')[0];
        let value = Number(room.split(' ')[1]);

        // You got some to snack!
        if (item_or_monster === 'potion') {
            if (value + health > 100) {
                let extra_health = (health + value) - 100;
                value -= extra_health;
            }
            health += value;
            console.log( `You healed for ${value} hp.`);
            console.log(`Current health: ${health} hp.`);
       }

        // Get them money!
        else if (item_or_monster === 'chest') {
            coins += value;
            console.log(`You found ${value} coins.`);
        }

        // Ready ... Shit ... Fight!
        else {
            health -= value;
            if (health > 0) {
                console.log(`You slayed ${item_or_monster}.`);
            } else {
                console.log(`You died! Killed by ${item_or_monster}.`);
                console.log(`Best room: ${i + 1}`);
                break;
            }
        }

    }

    if (health > 0) {
        console.log("You've made it!");
        console.log(`Coins: ${coins}`);
        console.log(`Health: ${health}`);
    }
}

mask(["rat 10|bat 20|potion 10|rat 10|chest 100|boss 70|chest 1000"]);
// You slayed rat.
// You slayed bat.
// You healed for 10 hp.
// Current health: 80 hp.
// You slayed rat.
// You found 100 coins.
// You died! Killed by boss.
// Best room: 6

console.log('---------------------------------')

mask(["cat 10|potion 30|orc 10|chest 10|snake 25|chest 110"]);
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
