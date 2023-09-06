function mask (names) {
    // MASK
    class Employee{
        constructor(name) {
            this.name = name;
            this.personalNumber = name.length;
        }

        presentYourself() {
            return `Name: ${this.name} -- Personal Number: ${this.personalNumber}`;
        }
    }


    let employees = [];


    names.forEach(name => {employees.push(new Employee(name))});
    employees.forEach(emp => {console.log(emp.presentYourself());});
}

mask([
'Silas Butler',
'Adnaan Buckley',
'Juan Peterson',
'Brendan Villarreal'
]);
// Name: Silas Butler -- Personal Number: 12
// Name: Adnaan Buckley -- Personal Number: 14
// Name: Juan Peterson -- Personal Number: 13
// Name: Brendan Villarreal -- Personal Number: 18

console.log('-------------------------------------');

mask([
'Samuel Jackson',
'Will Smith',
'Bruce Willis',
'Tom Holland'
]);
// Name: Samuel Jackson -- Personal Number: 14
// Name: Will Smith -- Personal Number: 10
// Name: Bruce Willis -- Personal Number: 12
// Name: Tom Holland -- Personal Number: 11


