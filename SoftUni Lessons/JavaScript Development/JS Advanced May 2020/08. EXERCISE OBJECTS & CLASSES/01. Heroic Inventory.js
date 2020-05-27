function heroicInventory(input) {
    // Mask - https://git.io/Jfre1
    let heroes = [];  // for safe keep :D

    class Hero {
        constructor(name = '', level = 0, items = []) {
            this.name = name;
            this.level = level;
            this.items = items;
        }
    }

    for (const data of input) {
        let name = data.split(' / ')[0];
        let level = Number(data.split(' / ')[1]);
        let items = data.split(' / ').length > 2 ? data.split(' / ')[2].split(', ') : [];

        let hero = new Hero(name, level, items);
        heroes.push(hero);
    }

    console.log(JSON.stringify(heroes));
}

heroicInventory([
    'Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara']
);
// Should return:
// [{"name":"Isacc","level":25,"items":["Apple","GravityGun"]},{"name":"Derek","level":12,"items":["BarrelVest","DestructionSword"]},{"name":"Hes","level":1,"items":["Desolator","Sentinel","Antara"]}]

heroicInventory(['Jake / 1000 / Gauss, HolidayGrenade']);
// Should return:
// [{"name":"Jake","level":1000,"items":["Gauss","HolidayGrenade"]}]
