function employees(input) {
    // Mask
    function variantWithClass(input) {
        // If you want to use this way just uncomment it from the main function.
        // And comment the variant with object
        let office = [];  // Here we will keep all the objects

        class Employee {
            constructor(name) {
                this.name = name;
                this.number = name.length;
            }

            print() {
                console.log(`Name: ${this.name} -- Personal Number: ${this.number}`);
            }
        }

        for (let employee of input) {
            office.push(new Employee(employee, employee.length));
        }

        office.map((employee) => employee.print());
    }

    function variantWithObject(input) {
        // If you want to use this way just uncomment it from the main function.
        // And comment the variant with class
        let employee = {};

        input.map((name) => employee[name] = name.length);

        for (let [name, number] of Object.entries(employee)) {
            console.log(`Name: ${name} -- Personal Number: ${number}`);
        }
    }

    function main(input) {
        // SElect one of the two by commenting the line you dont want.
        // variantWithClass(input);
        variantWithObject(input);
    }

    main(input);
}

employees(['Silas Butler', 'Adnaan Buckley', 'Juan Peterson', 'Brendan Villarreal']);
// Should return:
// Name: Silas Butler -- Personal Number: 12
// Name: Adnaan Buckley -- Personal Number: 14
// Name: Juan Peterson -- Personal Number: 13
// Name: Brendan Villarreal -- Personal Number: 18
