// Short link: https://git.io/JfQ1b

class Company {
    constructor () {
        this.departments = [];
    }

    addEmployee(username, salary, position, department) {
        if (!username || !salary || !position || !department) {
            throw new Error('Invalid input!');
        } else if (salary < 0) {
            throw new Error('Invalid input!');
        }
        
        let emp = {username: username, salary: salary, position: position, department: department};
        this.departments.push(emp);
        return `New employee is hired. Name: ${username}. Position: ${position}`;
    }

    bestDepartment() {
        let bestDepartment = '';
        let bestAverageSalary = 0;
        
        let deps = {};
        for (const emp of this.departments) {
            if (deps[emp.department]) {
                deps[emp.department].push(emp);
            } else {
                deps[emp.department] = [];
                deps[emp.department].push(emp);
            }
        }

        for (let [department, employees] of Object.entries(deps)) {
            let currentSalary = 0;
            for (let emp of employees) {
                currentSalary += emp.salary;
            }
            let currentAverageSalary = currentSalary / employees.length;
            if (currentAverageSalary > bestAverageSalary) {
                bestAverageSalary = currentAverageSalary;
                bestDepartment = department
            }
        }
        let bestDep = deps[bestDepartment];

        let result = '';
        result += `Best Department is: ${bestDepartment}`;
        result += `\nAverage salary: ${bestAverageSalary.toFixed(2)}`;

        for (let emp of bestDep.sort((a, b) => {
            return b.salary - a.salary || a.username.localeCompare(b.username);
        })) {
            result += `\n${emp.username} ${emp.salary} ${emp.position}`;
        }
        return result;
    }
}

let c = new Company();
c.addEmployee("Stanimir", 2000, "engineer", "Human resources")
c.addEmployee("Pesho", 1500, "electrical engineer", "Construction");
c.addEmployee("Slavi", 500, "dyer", "Construction");
c.addEmployee("Stan", 2000, "architect", "Construction");
c.addEmployee("Stanimir", 1200, "digital marketing manager", "Marketing");
c.addEmployee("Pesho", 1000, "graphical designer", "Marketing");
c.addEmployee("Gosho", 1350, "HR", "Human resources");
console.log(c.bestDepartment());



function toDO() {
    // I have started splitting the task in separated classes:
    // Maybe I will finish it in the future for now:
    class Company {
        constructor() {
            this.departments = [];
        }

        addEmployee(username, salary, position, department) {
            let employee = new Employee (username, salary, position, department);
            this.departments.push(employee);
            return `New employee is hired. Name: ${username}. Position: ${position}`;
        }

        bestDepartment() {
            // TODO...
        }
    }

    class Employee {
        constructor(username, salary, position, department) {
            this.username = username;
            this.salary = salary;
            this.position = position;
            this.department = department;
        }
        get username() { return this._username; }
        set username(newName) { newName ? this._username = newName : Employee.throwError(); }

        get salary () { return this._salary; }
        set salary (newSalary) { newSalary && Number(newSalary) > 0 ? this._salary = Number(newSalary) : Employee.throwError(); }

        get position() { return this._position; }
        set position(newPosition) { newPosition ? this._position = newPosition : Employee.throwError(); }

        get department() { return this._department; }
        set department(newDepartment) { newDepartment ? this._department = newDepartment : Employee.throwError(); }

        static throwError() { throw new Error('Invalid input!'); }
    }

    let c = new Company();
    c.addEmployee("Stanimir", 2000, "engineer", "Human resources");
    c.addEmployee("Pesho", 1500, "electrical engineer", "Construction");
}
