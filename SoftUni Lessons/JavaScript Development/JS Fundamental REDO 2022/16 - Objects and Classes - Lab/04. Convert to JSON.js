function convertToJson (name, lastName, hairColor) {
    // MasK
    class Person {
        constructor(name, lastName, harColor) {
            this.name = name;
            this.lastName = lastName;
            this.hairColor = harColor;
        }
    }
    console.log(JSON.stringify(new Person(name, lastName, hairColor)));
}

convertToJson('George', 'Jones', 'Brown');
// {"name":"George","lastName":"Jones","hairColor":"Brown"}