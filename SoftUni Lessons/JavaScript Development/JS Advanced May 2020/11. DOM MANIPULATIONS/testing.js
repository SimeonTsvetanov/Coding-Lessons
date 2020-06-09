class Person {
    constructor(firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.fullName =  function() {return `${this.firstName} ${this.lastName}`};
    }
}


let simeon = new Person('Simeon', 'Tsvetanov');
console.log(simeon.fullName());
// Return: Simeon Tsvetanov
simeon.firstName = 'Moni';
console.log(simeon.fullName());
// Return: Moni Tsvetanov

