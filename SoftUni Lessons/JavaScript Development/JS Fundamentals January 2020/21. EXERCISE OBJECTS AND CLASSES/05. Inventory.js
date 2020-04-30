function inventory(input) {
    // Mask
    let heroes = [];

    for (let details of input) {
        details = details.split(' / ')
        let name = details[0];
        let level = Number(details[1]);
        let items = details[2].split(', ');
        let hero = {name: name, level: level, items: items};
        heroes.push(hero);
    }

    for (let hero of heroes.sort((heroOne, heroTwo) => heroOne.level - heroTwo.level)) {
        console.log(`Hero: ${hero.name}`);
        console.log(`level => ${hero.level}`);
        console.log(`items => ${hero.items.sort().join(', ')}`);
    }
}


inventory([
        "Isacc / 25 / Apple, GravityGun",
        "Derek / 12 / BarrelVest, DestructionSword",
        "Hes / 1 / Desolator, Sentinel, Antara"
    ]
);
// Should return:
// Hero: Hes
// level => 1
// items => Antara, Desolator, Sentinel
// Hero: Derek
// level => 12
// items => BarrelVest, DestructionSword
// Hero: Isacc
// level => 25
// items => Apple, GravityGun
