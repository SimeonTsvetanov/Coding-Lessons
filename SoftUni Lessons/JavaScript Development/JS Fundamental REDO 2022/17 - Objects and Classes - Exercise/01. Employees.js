function employees (data) {
    // MasK
    class Employee {
        constructor(name) {
            this.name = name
        }

        get personalNumber() {
            return this.name.length;
        }

        toString = () => {
            return `Name: ${this.name} -- Personal Number: ${this.personalNumber}`;
        }
    }

    let employees = [];

    data.forEach(name => {
        employees.push(new Employee(name));
    });

    employees.forEach(employee => {
        console.log(employee.toString());
    });
}

employees([
        'Silas Butler',
        'Adnaan Buckley',
        'Juan Peterson',
        'Brendan Villarreal'
    ]
);

// Name: Silas Butler -- Personal Number: 12
// Name: Adnaan Buckley -- Personal Number: 14
// Name: Juan Peterson -- Personal Number: 13
// Name: Brendan Villarreal -- Personal Number: 18
