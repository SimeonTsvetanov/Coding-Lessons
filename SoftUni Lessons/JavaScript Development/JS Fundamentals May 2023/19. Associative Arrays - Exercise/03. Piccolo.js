function mask (params) {
    // MASK
    let parking = [];
    params.forEach(param => {
        let [inOrOut, number] = param.split(', ');
        if ((!(parking.includes(number))) && (inOrOut === 'IN')) {
            parking.push(number);
        } else if ((parking.includes(number)) && (inOrOut === 'OUT')) {
            parking.splice(parking.indexOf(number), 1);
        }
    });

    let sorted = parking.sort();
    sorted.length > 0 ? console.log(parking.join(`\n`)) : console.log(`Parking Lot is Empty`);
}

mask(['IN, CA2844AA',
'IN, CA1234TA',
'OUT, CA2844AA',
'IN, CA9999TT',
'IN, CA2866HI',
'OUT, CA1234TA',
'IN, CA2844AA',
'OUT, CA2866HI',
'IN, CA9876HH',
'IN, CA2822UU']);
// CA2822UU
// CA2844AA
// CA9876HH
// CA9999TT

console.log('-------------------------------------');

mask(['IN, CA2844AA',
'IN, CA1234TA',
'OUT, CA2844AA',
'OUT, CA1234TA']);
// Parking Lot is Empty
