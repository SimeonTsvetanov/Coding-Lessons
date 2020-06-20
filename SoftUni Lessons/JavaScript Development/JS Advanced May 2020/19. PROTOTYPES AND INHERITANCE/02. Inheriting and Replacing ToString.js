function toStringExtension() {
    class Person {
        // The Person class should have a name and an email
        constructor(name, email) {
            this.name = name;
            this.email = email;
        }

        toString() {
            // Add toString() functions to all classes
            let result = `Person (name: ${this.name}, email: ${this.email})`;
            this.constructor.name === 'Student' ? result = `Student (name: ${this.name}, email: ${this.email}, course: ${this.course})` : 'pass';
            this.constructor.name === 'Teacher' ? result = `Teacher (name: ${this.name}, email: ${this.email}, subject: ${this.subject})` : 'pass';
            return result;
        }
    }

    class Teacher extends Person{
        // The Teacher class should have a name, an email, and a subject
        constructor(name, email, subject) {
            super(name, email);
            this.subject = subject;
        }
    }

    class Student extends Person {
        // The Student class should have a name, an email, and a course
        constructor(name, email, course) {
            super(name, email);
            this.course = course;
        }
    }

    return {
        Person,
        Teacher,
        Student
    };
}

toStringExtension();