class Person {
    // Mask - https://git.io/Jfo8b
    constructor(firstName, lastName, age, email) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        this.email = email;
    }

    toString() {
        return `${this.firstName} ${this.lastName} (age: ${this.age}, email: ${this.email})`;
    }
}

let person = new Person('Anna', 'Simpson', 22, 'anna@yahoo.com');

console.log(person.toString());
// Should be: Anna Simpson (age: 22, email: anna@yahoo.com)
