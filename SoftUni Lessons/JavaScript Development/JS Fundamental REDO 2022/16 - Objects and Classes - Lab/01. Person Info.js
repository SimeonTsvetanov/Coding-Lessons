function personInfo(firstName, lastName, age) {
    // MasK
    class Person {
        constructor(firstName, lastName, age) {
            this.firstName = firstName;
            this.lastName = lastName;
            this.age = age;
        }
    }

    return new Person(firstName, lastName, age);
}

let person = personInfo("Peter",
    "Pan",
    "20"
)

console.log(person);