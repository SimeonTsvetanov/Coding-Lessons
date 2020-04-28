function cats(array) {
    // Mask
    class Cat {
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }
        meow() {
            return `${this.name}, age ${this.age} says Meow`;
        }
    }

    let catsOnlyArray = [];

    for (let catDetails of array) {
        let [name, age] = catDetails.split(' ');
        catsOnlyArray.push(new Cat(name, age));
    }

    for (let cat of catsOnlyArray) {
        console.log(cat.meow());
    }
}

cats(['Mellow 2', 'Tom 5']);  // Should return:
// Mellow, age 2 says Meow
// Tom, age 5 says Meow
