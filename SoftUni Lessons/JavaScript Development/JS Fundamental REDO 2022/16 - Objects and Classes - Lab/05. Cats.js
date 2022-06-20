function cats (data) {
    // MasK
    class Cat {
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }

        meow() {
            console.log(`${this.name}, age ${this.age} says Meow`);
        }
    }

    data.forEach(cat => {
        let [name, age] = cat.split(' ');
        new Cat(name, age).meow();
    });
}

cats(['Mellow 2', 'Tom 5']);
// Mellow, age 2 says Meow
// Tom, age 5 says Meow
