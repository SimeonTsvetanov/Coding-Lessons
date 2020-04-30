function makeADictionary(input) {
    // Mask
    let dictionary = [];

    for (let data of input) {
        let object = JSON.parse(data);
        for (let [name, definition] of Object.entries(object)) {
            let term = {name: name, definition: definition};

            let included = false;
            for (let oldTerm of dictionary) {
                if (oldTerm.name === term.name) {
                    oldTerm.definition = term.definition;
                    included = true;
                }
            }

            if (!included) {
                dictionary.push(term);
            }
        }
    }

    dictionary.sort((a, b) => a.name.localeCompare(b.name));

    for (let term of dictionary) {
        console.log(`Term: ${term.name} => Definition: ${term.definition}`);
    }
}

makeADictionary([
        '{"Coffee":"A hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub."}',
        '{"Bus":"A large motor vehicle carrying passengers by road, typically one serving the public on a fixed route and for a fare."}',
        '{"Boiler":"A fuel-burning apparatus or container for heating water."}',
        '{"Tape":"A narrow strip of material, typically used to hold or fasten something."}',
        '{"Microphone":"An instrument for converting sound waves into electrical energy variations which may then be amplified, transmitted, or recorded."}'
    ]
);  // Should return:
// Term: Boiler => Definition: A fuel-burning apparatus or container for heating water.
//     Term: Bus => Definition: A large motor vehicle carrying passengers by road, typically one serving the public on a fixed route and for a fare.
//     Term: Coffee => Definition: A hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub.
//     Term: Microphone => Definition: An instrument for converting sound waves into electrical energy variations which may then be amplified, transmitted, or recorded.
//     Term: Tape => Definition: A narrow strip of material, typically used to hold or fasten something.
