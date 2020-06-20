function PersonAndTeacher() {
    class Person {
        // The Person class should have a name and an email
        constructor(name, email) {
            this.name = name;
            this.email = email;
        }
    }

    class Teacher extends Person{
        // The Teacher class should have a name, an email, and a subject
        constructor(name, email, subject) {
            super(name, email);
            this.subject = subject;
        }
    }

    return {
        // Return an object containing the classes Person and Teacher
        Person,
        Teacher,
    }
}