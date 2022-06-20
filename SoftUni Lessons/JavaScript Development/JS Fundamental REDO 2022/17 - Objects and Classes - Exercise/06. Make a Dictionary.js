function makeADictionary (data) {
    // MasK
    let dict = [];  // Create the dict!

    // Fetch and sort the data:
    data.forEach(term => {
        let parsed = JSON.parse(term);  // Parse the JSON to JS Object
        let [key, value] = Object.entries(parsed)[0];  // Get the key and value of the object

        // Check if we already have the term in the dict:
        let alreadyIncluded = dict.find(a => {
            return a.term === key;
        });

        if (alreadyIncluded) {
            alreadyIncluded.definition = value;  // If we have it just change the vale
        } else {
            dict.push({term: key, definition: value});  // If we don't have it: append it!
        }
    });

    // Sort the dict:
    dict.sort((a, b) => a.term.localeCompare(b.term));

    // Print the dict:
    dict.forEach(x => {
        console.log(`Term: ${x.term} => Definition: ${x.definition}`);
    });
}

makeADictionary([
        '{"Coffee":"A hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub."}',
        '{"Bus":"A large motor vehicle carrying passengers by road, typically one serving the public on a fixed route and for a fare."}',
        '{"Boiler":"A fuel-burning apparatus or container for heating water."}',
        '{"Tape":"A narrow strip of material, typically used to hold or fasten something."}',
        '{"Microphone":"An instrument for converting sound waves into electrical energy variations which may then be amplified, transmitted, or recorded."}'
    ]
);

// Term: Boiler => Definition: A fuel-burning apparatus or container for heating water.
// Term: Bus => Definition: A large motor vehicle carrying passengers by road, typically one serving the public on a fixed route and for a fare.
// Term: Coffee => Definition: A hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub.
// Term: Microphone => Definition: An instrument for converting sound waves into electrical energy variations which may then be amplified, transmitted, or recorded.
// Term: Tape => Definition: A narrow strip of material, typically used to hold or fasten something.

console.log(`------------------------------------`);

makeADictionary([
        '{"Cup":"A small bowl-shaped container for drinking from, typically having a handle"}',
        '{"Cake":"An item of soft sweet food made from a mixture of flour, fat, eggs, sugar, and other ingredients, baked and sometimes iced or decorated."} ',
        '{"Watermelon":"The large fruit of a plant of the gourd family, with smooth green skin, red pulp, and watery juice."} ',
        '{"Music":"Vocal or instrumental sounds (or both) combined in such a way as to produce beauty of form, harmony, and expression of emotion."} ',
        '{"Art":"The expression or application of human creative skill and imagination, typically in a visual form such as painting or sculpture, producing works to be appreciated primarily for their beauty or emotional power."} '
    ]
);

// Term: Art => Definition: The expression or application of human creative skill and imagination, typically in a visual form such as painting or sculpture, producing works to be appreciated primarily for their beauty or emotional power.
// Term: Cake => Definition: An item of soft sweet food made from a mixture of flour, fat, eggs, sugar, and other ingredients, baked and sometimes iced or decorated.
// Term: Cup => Definition: A small bowl-shaped container for drinking from, typically having a handle
// Term: Music => Definition: Vocal or instrumental sounds (or both) combined in such a way as to produce beauty of form, harmony, and expression of emotion.
// Term: Watermelon => Definition: The large fruit of a plant of the gourd family, with smooth green skin, red pulp, and watery juice.

