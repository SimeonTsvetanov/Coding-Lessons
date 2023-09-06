function mask (...params) {
    // MASK
    class Town{
        constructor(name, population, area) {
            this.name = name;
            this.population = population;
            this.area = area;
        }

        getDetails() {
            return (`Town ${this.name} has population of ${this.population} and area ${this.area} square km.`);
        }
    }

    let town = new Town(params[0], params[1], params[2]);
    console.log(town.getDetails());
}

mask('Sofia',
1286383,
492
);
// Town Sofia has population of 1286383 and area 492 square km.

mask('Plovdiv',
1481353,
512
);
// Town Plovdiv has population of 1481353 and area 512 square km.
