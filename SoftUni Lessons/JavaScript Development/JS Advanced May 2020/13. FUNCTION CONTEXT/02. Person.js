class Person {
    constructor (firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }
    get fullName() {
        return this.firstName + ' ' + this.lastName;
    }

    set fullName (newName) {
        let names = newName.split(' ');
        if (names.length !== 2) { return; }
        this.firstName = names[0];
        this.lastName = names[1];
    }
}

let person = new Person("Albert", "Simpson");
console.log(person.fullName);//Albert Simpson
person.firstName = "Simon";
console.log(person.fullName);//Simon Simpson
person.fullName = "Peter";
console.log(person.firstName) // Simon
console.log(person.lastName) // Simpson
 