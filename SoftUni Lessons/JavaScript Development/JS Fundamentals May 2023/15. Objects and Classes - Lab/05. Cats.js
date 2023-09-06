function mask (params) {
    // MASK
    let cats = params;

    class Cat{
        constructor(name, age) {
            this.name = name;
            this.age = Number(age);
        }

        meow() {
            console.log(`${this.name}, age ${this.age} says Meow`);
        }
    }

    cats.forEach(data => {
        let [name, age] = data.split(' ');
        const cat = new Cat(name, age);
        cat.meow();
    });

}

mask(['Mellow 2', 'Tom 5']);
// Mellow, age 2 says Meow
// Tom, age 5 says Meow

console.log('-------------------------------------');

mask(['Candy 1', 'Poppy 3', 'Nyx 2']);
// Candy, age 1 says Meow
// Poppy, age 3 says Meow
// Nyx, age 2 says Meow
