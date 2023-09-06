function mask (firstName, lastName, age) {
    // MASK
    class Person {
        constructor(firstName, lastName, age) {
            this.firstName = firstName;
            this.lastName = lastName;
            this.age = Number(age);
        }

        introduceSelf() {
            console.log(`firstName: ${this.firstName}`);
            console.log(`lastName: ${this.lastName}`);
            console.log(`age: ${this.age}`);
        }
    }

    let person = new Person(firstName, lastName, age);
    return person
}

mask("Peter",
"Pan",
"20");
// firstName: Peter
// lastName: Pan
// age: 20

console.log('-------------------------------------');

mask("George",
"Smith",
"18"
);
// firstName: George
// lastName: Smith
// age: 18
