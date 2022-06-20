function inventory (data) {
    // MasK
    let heroes = [];  // To keep All the heroes:

    data.forEach(command => {
        // Let's fetch the needed data:
        let name = command.split(' / ')[0];
        let level = Number(command.split(' / ')[1]);
        let items = command.split(' / ')[2].split(', ');

        let hero = {};  // Create the object

        // Fill with the given data:
        hero.name = name;
        hero.level = level;
        hero.items = []
        items.forEach(item => {
            hero.items.push(item);
        });

        heroes.push(hero);  // Add the hero to the array!
    });

    // Sort the Heroes:
    heroes.sort((a, b) => a.level - b.level)

    // Print the Heroes:
    heroes.forEach(hero => {
        console.log(`Hero: ${hero.name}`);
        console.log(`level => ${hero.level}`);
        console.log(`items => ${hero.items.join(', ')}`);  // TODO Check if we have to add items print
    });
}

inventory([
        'Isacc / 25 / Apple, GravityGun',
        'Derek / 12 / BarrelVest, DestructionSword',
        'Hes / 1 / Desolator, Sentinel, Antara'
]);

// Hero: Hes
// level => 1
// items => Desolator, Sentinel, Antara
// Hero: Derek
// level => 12
// items => BarrelVest, DestructionSword
// Hero: Isacc
// level => 25
// items => Apple, GravityGun
