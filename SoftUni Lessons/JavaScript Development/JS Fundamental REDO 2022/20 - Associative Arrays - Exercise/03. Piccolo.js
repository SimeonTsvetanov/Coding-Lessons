function piccolo (data) {
    // MasK --> Unclear how to sort the cars in the output! It's needed to be by the full reg alphabetically!!!!

    class Parking {
        constructor() {
            this.cars = [];
        }

        addCar (newCar) {
            let carPresent = this.cars.find(car => {return car.registration === newCar.registration});
            if (!carPresent) {
                this.cars.push(newCar)
            }
        }

        removeCar (oldCar) {
            let carPresent = this.cars.find(car => {return car.registration === oldCar.registration});
            if (carPresent) {
                this.cars.splice(this.cars.indexOf(carPresent), 1);
            }
        }

        sortParking() {
            this.cars.sort((a, b) => a.registration.localeCompare(b.registration));
        }

        print() {
            if (this.cars.length === 0) {
                console.log(`Parking Lot is Empty`);
            } else {
                this.cars.forEach(car => {
                    console.log(car.registration);
                });
            }
        }
    }

    class Car {
        constructor(registration, number) {
            this.registration = registration;
            this.number = number;
        }
    }

    let parking = new Parking();

    data.forEach(command => {
        let [direction, reg] = command.split(', ');
        let currentCar = new Car(reg, Number(reg.slice(2, 6)));

        direction === 'IN' ? parking.addCar(currentCar) : parking.removeCar(currentCar);
    });

    parking.sortParking();
    parking.print();
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
);
// CA2822UU
// CA2844AA
// CA9876HH
// CA9999TT

console.log();

piccolo(['IN, CA2844AA',
    'IN, CA1234TA',
    'OUT, CA2844AA',
    'OUT, CA1234TA']
);

console.log();
