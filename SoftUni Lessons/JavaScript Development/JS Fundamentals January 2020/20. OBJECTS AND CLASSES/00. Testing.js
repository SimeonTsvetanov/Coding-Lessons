class Person {
    constructor(firstName, lastName, age, gender) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        this.gender = gender;
    }

    introduceYourSelf () {
        console.log(`Hello, my name is ${this.firstName} ${this.lastName} and I'am ${this.age} years old ${this.gender}`);
    }
}

mask = new Person('Simeon', 'Tsvetanov', 30, 'male');

mask.introduceYourSelf();
