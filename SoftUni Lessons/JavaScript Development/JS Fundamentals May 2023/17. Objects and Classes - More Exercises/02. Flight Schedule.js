function mask (params) {
    // MASK - solved not using the intended logic with nested objects. But I think this way is better.

    // The first array (at index 0) will hold all flights on a specific sector in the airport
    let flightsInput = params[0];
    // The second array (at index 1) will contain newly changed statuses of some of the flights at this airport.
    let changedStatusesInput = params[1];
    // The third array (at index 2) will have a single string, which will be the flight status you need to check.
    let flightStatus = params[2];

    // When you put all flights into an object
    let flights = [];
    flightsInput.forEach(flightData => {
        let [number, destination] = flightData.split(' ');
        flights.push({'number': number, 'destination': destination, 'status': 'Ready to fly'});
    });

    // change the statuses depends on the new information on the second array
    changedStatusesInput.forEach(data => {
        let [number, status] = data.split(' ');
        let flight = flights.find(x => x.number === number);
        (flight) ? flight.status = 'Cancelled' : 'pass';
    });

    // You must print all flights with the given
    // status from the last array.
    // • If the value of the string obtained from the third array is "Ready to fly":
    //      o then you must print flights that have not changed their status in the second array
    //      o and automatically change the status to "Ready to fly"
    // • Otherwise, print only flights that have changed their status.
    flights.forEach(flight => {
        if (flight.status == flightStatus) {
            console.log(`{ Destination: '${flight.destination}', Status: '${flight.status}' }`);
        }
    });
}

mask([['WN269 Delaware',
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
'SK430 Cancelled'],
['Cancelled']
]);
// { Destination: 'Alabama', Status: 'Cancelled' }
// { Destination: 'California', Status: 'Cancelled' }
// { Destination: 'Texas', Status: 'Cancelled' }

console.log('-------------------------------------');

mask([['WN269 Delaware',
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
]);
// { Destination: 'Delaware', Status: 'Ready to fly' }
// { Destination: 'Oregon', Status: 'Ready to fly' }
// { Destination: 'Las Vegas', Status: 'Ready to fly'
// }
// { Destination: 'Ohio', Status: 'Ready to fly' }
// { Destination: 'New York', Status: 'Ready to fly' }
// { Destination: 'Illinois', Status: 'Ready to fly' }
// { Destination: 'Pennsylvania', Status: 'Ready to
// fly' }
