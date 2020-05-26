// let person = {
//     firstName: 'Simeon',
//     lastName: 'Tsvetanov',
//     age: 30,
//     town: 'Smolyan',
//     fullName: function () {
//         return `${this.firstName} ${this.lastName}`
//     },
//     car: 'Toyota RAV4',
// };

//
// console.log(person.firstName);
// console.log(person['lastName']);
// console.log(person.fullName());
// console.log(person.car);
// delete person.car;
// console.log(person.car);
//
// console.log(JSON.stringify(person));
//
// Object.freeze(person);
// person.firstName = 'Moni';
// console.log(person.firstName);
//
// let keys = Object.keys(person)
// console.log(keys);
// let values = Object.values(person)
// console.log(values);
//
// for (let [key, value] of Object.entries(person)) {
//     console.log(key + ": " + value);
// }

// class Person {
//     constructor(firstName, lastName, age) {
//         this.firstName = firstName;
//         this.lastName = lastName;
//         this.age = age;
//     }
// }
//
// simeon = new Person('Simeon', 'Tsvetanov, 30');
// simeon.car = 'Toyota';
//
// console.log(simeon.car);


// class Person {
//     constructor(firstName, lastName, age, email) {
//         this.firstName = firstName;
//         this.lastName = lastName;
//         this.age = age;
//         this.email = email;
//     }
//
//     toString() {
//         return `${this.firstName} ${this.lastName} (age: ${this.age}, email: ${this.email})`;
//     }
// }
//
// let person = new Person('Anna', 'Simpson', 22, 'anna@yahoo.com');
//
// // console.log(person.toString());
// // Should be: Anna Simpson (age: 22, email: anna@yahoo.com)
//
// class Child extends Person {
//     constructor(firstName, lastName, age, email, subject) {
//         super(firstName, lastName, age, email);
//         this.subject = subject;
//     }
// }
//
// moni = new Child('Moni', 'Tsvetanov', 30, 'tsvetanov.simeon"gmail.com', 'wild');
//
// console.log(moni.toString());

class Circle {
    constructor(radius) { this.radius = radius; }
    get diameter() { return 2 * this.radius; }
    set diameter(diameter) {
        this.radius = diameter / 2;
    }
    get area() {
        return Math.PI * this.radius * this.radius;
    }


}

circle = new Circle(3);

console.log(circle.radius);
console.log(circle.diameter);
console.log(circle.area);