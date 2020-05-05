function piccolo(input) {
    // Mask - There are two ways to solve the task. Check the end of the function.

    function arraySolution (input) {
        // First solution from at home.
        let parking = [];

        input.forEach(command => {
            let [direction, reg] = command.split(', ');
            if (direction === 'IN') {
                if (!parking.includes(reg)) {parking.push(reg);}
            } else {
                if (parking.includes(reg)) {parking.splice(parking.indexOf(reg), 1);}
            }
        })

        let sorted = parking.sort();

        sorted.length > 0 ? console.log(parking.join(`\n`)) : console.log(`Parking Lot is Empty`);
    }

    function inClassSolution(input) {
        // Second Solution from in Class using Object:

        function fillParkingInfo(input) {
            let parking = {};
            input.forEach(line => {
                let car = line.split(', ');
                parking[car[1]] = car[0];
            })
            return parking;
        }

        function filterCarsIn(parking) {
            let output = [];
            Object.entries(parking).forEach(entry => {
                if(entry[1] === 'IN') {
                    output.push(entry[0]);
                }
            })
            return output;
        }

        function getOutput(arr) {
            return arr.length === 0
            ? 'Parking Lot is Empty'
            : arr.sort((a, b) => a.localeCompare(b)).join("\n");
        }

        let parking = fillParkingInfo(input);
        let output = filterCarsIn(parking);
        return getOutput(output);
    }

    // To use one of the functions just uncomment it, and comment the other one:
    // arraySolution(input);
    console.log(inClassSolution(input));
}

piccolo(['IN, CA2844AA',
    'IN, CA1234TA',
    'OUT, CA2844AA',
    'IN, CA9999TT',
    'IN, CA2866HI',
    'OUT, CA1234TA',
    'IN, CA2844AA',
    'OUT, CA2866HI',
    'IN, CA9876HH',
    'IN, CA2822UU']
);  // Should return:
// CA2822UU
// CA2844AA
// CA9876HH
// CA9999TT


piccolo(['IN, CA2844AA',
    'IN, CA1234TA',
    'OUT, CA2844AA',
    'OUT, CA1234TA']
);  // Should return:
// Parking Lot is Empty