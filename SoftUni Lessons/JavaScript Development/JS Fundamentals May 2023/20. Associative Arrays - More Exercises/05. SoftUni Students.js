function mask (params) {
    // MASK
    class School {
        constructor() {
            this.courses = []
        }

        fillData(params) {
            params.forEach(param => {
                if (param.includes(": ")) {
                    // Add or update Course:
                    let name = param.split(": ")[0];
                    let capacity = Number(param.split(": ")[1]);
                    this.addCourse(name, capacity);
                } else {
                    // Add or update Student:
                    let studentName = param.split('[')[0];
                    let credits = Number(param.split(" with email ")[0].split("[")[1].replace(']', ''));
                    let email = param.split(' with email ')[1].split(' joins ')[0];
                    let courseName = param.split(' with email ')[1].split(' joins ')[1];
                    this.addStudent(new Student(studentName, credits, email), courseName);
                }
            });
        }

        addCourse(name, capacity) {
            let presentCourse = this.courses.find(x => x.name === name)
            if (presentCourse) { presentCourse.capacity += capacity; }
            else { this.courses.push(new Course(name, capacity)); }
        }

        addStudent(student, course) {
            let presentCourse = this.courses.find(x => x.name === course);
            if (presentCourse) {
                if (presentCourse.capacity > presentCourse.students.length) {
                    presentCourse.students.push(student);
                }
            }
        }

        print() {
            for (let course of this.courses.sort((a, b) => b.students.length - a.students.length)) {
                console.log(`${course.name}: ${course.capacity - course.students.length} places left`);
                for (let student of course.students.sort((a, b) => b.credits - a.credits)) {
                    console.log(`--- ${student.credits}: ${student.name}, ${student.email}`);
                }
            }
        }
    }

    class Course {
        constructor(name, capacity) {
            this.name = name;
            this.capacity = capacity;
            this.students = [];
        }

        get placesLeft() {
            return this.capacity - this.students.length;
        }
    }

    class Student {
        constructor(name, credits, email) {
            this.name = name;
            this.credits = credits;
            this.email = email;
        }
    }

    let softuni = new School();
    softuni.fillData(params);
    softuni.print();
}

mask([
    'JavaBasics: 2',
    'user1[25] with email user1@user.com joins C#Basics',
    'C#Advanced: 3',
    'JSCore: 4',
    'user2[30] with email user2@user.com joins C#Basics',
    'user13[50] with email user13@user.com joins JSCore',
    'user1[25] with email user1@user.com joins JSCore',
    'user8[18] with email user8@user.com joins C#Advanced',
    'user6[85] with email user6@user.com joins JSCore',
    'JSCore: 2',
    'user11[3] with email user11@user.com joins JavaBasics',
    'user45[105] with email user45@user.com joins JSCore',
    'user007[20] with email user007@user.com joins JSCore',
    'user700[29] with email user700@user.com joins JSCore',
    'user900[88] with email user900@user.com joins JSCore'
    ]);
// JSCore: 0 places left
// --- 105: user45, user45@user.com
// --- 85: user6, user6@user.com
// --- 50: user13, user13@user.com
// --- 29: user700, user700@user.com
// --- 25: user1, user1@user.com
// --- 20: user007, user007@user.com
// JavaBasics: 1 places left
// --- 3: user11, user11@user.com
// C#Advanced: 2 places left
// --- 18: user8, user8@user.com

console.log('-------------------------------------');

mask([
    'JavaBasics: 15',
    'user1[26] with email user1@user.com joins JavaBasics',
    'user2[36] with email user11@user.com joins JavaBasics',
    'JavaBasics: 5',
    'C#Advanced: 5',
    'user1[26] with email user1@user.com joins C#Advanced',
    'user2[36] with email user11@user.com joins C#Advanced',
    'user3[6] with email user3@user.com joins C#Advanced',
    'C#Advanced: 1',
    'JSCore: 8',
    'user23[62] with email user23@user.com joins JSCore'
]);
// C#Advanced: 3 places left
// --- 36: user2, user11@user.com
// --- 26: user1, user1@user.com
// --- 6: user3, user3@user.com
// JavaBasics: 18 places left
// --- 36: user2, user11@user.com
// --- 26: user1, user1@user.com
// JSCore: 7 places left
// --- 62: user23, user23@user.com
