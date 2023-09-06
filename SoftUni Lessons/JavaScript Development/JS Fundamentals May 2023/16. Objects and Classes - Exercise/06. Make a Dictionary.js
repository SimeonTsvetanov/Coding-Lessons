function mask (params) {
    // MASK
    let dict = [];

    params.forEach(param => {
        let obj = JSON.parse(param);
        let t = Object.keys(obj)[0];
        let d = Object.values(obj)[0];

        let term = dict.find(x => {return x.term === t});
        if (term) {
            term['definition'] = d;
        } else {
            dict.push({'term': t, 'definition': d});
        }
    });

    dict.sort((a, b) => a.term.localeCompare(b.term));

    dict.forEach(t => {
        console.log(`Term: ${t.term} => Definition: ${t.definition}`);
    });
}

mask([
'{"Coffee":"A hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub."}',
'{"Bus":"A large motor vehicle carrying passengers by road, typically one serving the public on a fixed route and for a fare."}',
'{"Boiler":"A fuel-burning apparatus or container for heating water."}',
'{"Tape":"A narrow strip of material, typically used to hold or fasten something."}',
'{"Microphone":"An instrument for converting sound waves into electrical energy variations which may then be amplified, transmitted, or recorded."}'
]);
// Term: Boiler => Definition: A fuelburning apparatus or container for
// heating water.
// Term: Bus => Definition: A large motor
// vehicle carrying passengers by road,
// typically one serving the public on a
// fixed route and for a fare.
// Term: Coffee => Definition: A hot drink
// made from the roasted and ground seeds
// (coffee beans) of a tropical shrub.
// Term: Microphone => Definition: An
// instrument for converting sound waves
// into electrical energy variations which
// may then be amplified, transmitted, or
// recorded.
// Term: Tape => Definition: A narrow
// strip of material, typically used to
// hold or fasten something.

