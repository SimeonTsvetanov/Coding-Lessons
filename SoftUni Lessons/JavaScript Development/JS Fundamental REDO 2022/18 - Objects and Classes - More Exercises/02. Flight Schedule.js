function flightSchedule (data) {
    // MasK - Cool task, but missed explained problem description there are two missing edge cases !!!
    // Check the notes below for clarification.
    class Flight {
        constructor(number, destination) {
            this.number = number;
            this.destination = destination;
            this.status = undefined;
        }

        print() {
            return { Destination: this.destination, Status: this.status }
        }
    }

    let flights = []  // Keep all the flights here

    // Let's add the Flights:
    let flightsToAdd = data.shift();  // Extract the flights data
    flightsToAdd.forEach(flightData => {

        // !!! Edge case that is not in the Description: the destination can include space:
        let flightNumber = flightData.split(' ')[0];  // We get the flight number only!
        // And then we need to extract the rest of the data as one string to be the destination:
        let flightDestination = flightData.split(' ').slice(1, flightData.split(' ').length).join(' ');
        let flight = new Flight(flightNumber, flightDestination);  // Create the Flight object
        flights.push(flight);  // And push it in the array
    });

    // Let's check which flights will change Status:
    let changedStatus = data.shift();  // Collect the data!
    changedStatus.forEach(statusData => {
        let [number, status] = statusData.split(' ');
        let flightToChangeStatus = flights.find(flight => {return flight.number === number});

        /// !!! Edge case that's not in the description of the problem:
        // Check if the flight Exists:
        if (flightToChangeStatus) {
            // And if it does: Change the status of the flight:
            flightToChangeStatus.status = status;
        }
    });

    // Now get the status we need to print:
    let statusToPrint = data.shift()[0];

    // Check if the status is "Ready to fly":
    if (statusToPrint === 'Ready to fly') {
        // then you must print flights that have not changed their status in the second array and
        // automatically change the status to "Ready to fly"
        flights.forEach(flight => {
            if (!flight.status) {
                flight.status = "Ready to fly";  // Change the status
                console.log(flight.print());     // Print the flight information
            }
        });
    } else {
        // Otherwise, print only flights that have changed their status to the searched one:
        flights.forEach(flight => {
            if (flight.status === statusToPrint) {
                console.log(flight.print());  // Print the flight information
            }
        });
    }
}

// flightSchedule([['WN269 Delaware',
//         'FL2269 Oregon',
//         'WN498 Las Vegas',
//         'WN3145 Ohio',
//         'WN612 Alabama',
//         'WN4010 New York',
//         'WN1173 California',
//         'DL2120 Texas',
//         'KL5744 Illinois',
//         'WN678 Pennsylvania'],
//         ['DL2120 Cancelled',
//             'WN612 Cancelled',
//             'WN1173 Cancelled',
//             'SK430 Cancelled'],
//         ['Cancelled']
//     ]
// );

// { Destination: 'Alabama', Status: 'Cancelled' }
// { Destination: 'California', Status: 'Cancelled' }
// { Destination: 'Texas', Status: 'Cancelled' }

flightSchedule([['WN269 Delaware',
        'FL2269 Oregon',
        'WN498 Las Vegas',
        'WN3145 Ohio',
        'WN612 Alabama',
        'WN4010 New York',
        'WN1173 California',
        'DL2120 Texas',
        'KL5744 Illinois',
        'WN678 Pennsylvania'],
        ['DL2120 Cancelled',
            'WN612 Cancelled',
            'WN1173 Cancelled',
            'SK330 Cancelled'],
        ['Ready to fly']
    ]
);

// { Destination: 'Delaware', Status: 'Ready to fly' }
// { Destination: 'Oregon', Status: 'Ready to fly' }
// { Destination: 'Las Vegas', Status: 'Ready to fly' }
// { Destination: 'Ohio', Status: 'Ready to fly' }
// { Destination: 'New York', Status: 'Ready to fly' }
// { Destination: 'Illinois', Status: 'Ready to fly' }
// { Destination: 'Pennsylvania', Status: 'Ready to fly' }
