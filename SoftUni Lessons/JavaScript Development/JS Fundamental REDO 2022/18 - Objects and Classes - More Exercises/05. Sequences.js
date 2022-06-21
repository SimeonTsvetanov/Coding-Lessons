function sequences (data) {
    // MasK

    function arrayEquals(a, b) {
        a.sort((a, b) => a - b);
        b.sort((a, b) => a - b);
        return Array.isArray(a) &&
            Array.isArray(b) &&
            a.length === b.length &&
            a.every((val, index) => val === b[index]);
    }

    let arrays = [];

    data.forEach(inputArray => {
        let newArray = JSON.parse(inputArray);

        let unique = true;
        arrays.forEach(presentArray => {
            if (arrayEquals(presentArray, newArray)) {
                unique = false;
            }
        });

        if (unique) {
            arrays.push(newArray);
        }
    });

    // Sort The Arrays:
    arrays.sort((a, b) => {
        return a.length - b.length || 'pass';
    })

    // Print the Arrays:
    arrays.forEach(array => {
        // Sort the array:
        array.sort((a, b) => b - a);
        console.log(`[${array.join(', ')}]`);
    });
}

sequences(["[-3, -2, -1, 0, 1, 2, 3, 4]",
    "[10, 1, -17, 0, 2, 13]",
    "[4, -3, 3, -2, 2, -1, 1, 0]"]
);

sequences(["[7.14, 7.180, 7.339, 80.099]",
    "[7.339, 80.0990, 7.140000, 7.18]",
    "[7.339, 7.180, 7.14, 80.099]"]
);
