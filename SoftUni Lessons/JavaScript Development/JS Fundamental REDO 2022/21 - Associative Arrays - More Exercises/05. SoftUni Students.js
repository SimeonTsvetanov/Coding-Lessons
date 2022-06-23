function softUniStudents (data) {
    // MasK -- Done with Classes instead of Associative arrays!

    class Course {
        constructor(name, capacity) {
            this.name = name;
            this.capacity = capacity;
            this.students = [];
        }
    }

    class Student {
        constructor(username, credit, email) {
            this.username = username;
            this.credit = credit;
            this.email = email;
        }
    }

    let courses = [];

    function addCourse(name, capacity) {
        let presentCourse = courses.find(x => x.name === name);
        if (presentCourse) {
            presentCourse.capacity = presentCourse.capacity + capacity;
        } else {
            let newCourse = new Course(name, capacity);
            courses.push(newCourse);
        }
    }

    function addStudent(student, courseName) {
        let course = courses.find(x => x.name === courseName);
        if ((course) && (course.capacity - course.students.length >= 1)) {
            course.students.push(student);
        }
    }

    function printCourses() {
        courses.sort((a, b) => b.students.length - a.students.length);
        courses.forEach(course => {
            console.log(`${course.name}: ${course.capacity - course.students.length} places left`);
            course.students.sort((a, b) => b.credit - a.credit);
            course.students.forEach(student => {
                console.log(`--- ${student.credit}: ${student.username}, ${student.email}`);
            });
        });
    }

    data.forEach(entry => {
        if (entry.split(': ').length === 2) {
            // Add Course:
            let name = entry.split(': ')[0];
            let capacity = Number(entry.split(': ')[1]);
            addCourse(name, capacity);
        } else {
            // Add Student:
            let username = entry.split('[')[0];
            let credits = Number(entry.split("[")[1].split(']')[0]);
            let email = entry.split(' with email ')[1].split(' joins ')[0];
            let course = entry.split(' with email ')[1].split(' joins ')[1];

            let student = new Student(username, credits, email);
            addStudent(student, course);
        }
    });

    printCourses();
}

softUniStudents(['JavaBasics: 2', 'user1[25] with email user1@user.com joins C#Basics', 'C#Advanced: 3', 'JSCore: 4', 'user2[30] with email user2@user.com joins C#Basics', 'user13[50] with email user13@user.com joins JSCore', 'user1[25] with email user1@user.com joins JSCore', 'user8[18] with email user8@user.com joins C#Advanced', 'user6[85] with email user6@user.com joins JSCore', 'JSCore: 2', 'user11[3] with email user11@user.com joins JavaBasics', 'user45[105] with email user45@user.com joins JSCore', 'user007[20] with email user007@user.com joins JSCore', 'user700[29] with email user700@user.com joins JSCore', 'user900[88] with email user900@user.com joins JSCore']);
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

console.log('--------------------------------------');

softUniStudents(['JavaBasics: 15',
    'user1[26] with email user1@user.com joins JavaBasics',
    'user2[36] with email user11@user.com joins JavaBasics',
    'JavaBasics: 5',
    'C#Advanced: 5',
    'user1[26] with email user1@user.com joins C#Advanced',
    'user2[36] with email user11@user.com joins C#Advanced',
    'user3[6] with email user3@user.com joins C#Advanced',
    'C#Advanced: 1',
    'JSCore: 8',
    'user23[62] with email user23@user.com joins JSCore']
);
// C#Advanced: 3 places left
// --- 36: user2, user11@user.com
// --- 26: user1, user1@user.com
// --- 6: user3, user3@user.com
// JavaBasics: 18 places left
// --- 36: user2, user11@user.com
// --- 26: user1, user1@user.com
// JSCore: 7 places left
// --- 62: user23, user23@user.com
