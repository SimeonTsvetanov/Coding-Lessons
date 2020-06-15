function argumentsInfo(...arguments) {
    let dataTypes = {};

    // Get the Input sorted:
    arguments.map(arg => {
        let type = typeof(arg);
        let value = String(arg);
        console.log(`${type}: ${value}`);
        dataTypes.hasOwnProperty(type) ? dataTypes[type] += 1 : dataTypes[type] = 1;
    });

    // Sort and print the Output:
    Array
        .from(Object.keys(dataTypes))
        .sort((a, b) => dataTypes[b] - dataTypes[a])
        .map(type => {
            console.log(`${type} = ${dataTypes[type]}`);
        });
}

argumentsInfo({ name: 'bob'}, 3.333, 9.999);
