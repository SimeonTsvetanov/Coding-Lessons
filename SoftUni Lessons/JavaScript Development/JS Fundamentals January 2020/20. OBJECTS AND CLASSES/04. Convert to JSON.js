function convertToJSON(name, lastName, hairColor) {
    // Mask

    // NOTE! Here we can use only the given variables as they will
    // become the keys and the value they hold, will become values.
    // Cool! :D
    let person = {
        name,
        lastName,
        hairColor,
    }

    console.log(JSON.stringify(person));
}

convertToJSON('George', 'Jones', 'Brown');  // Should return:
// {"name":"George", "lastName":"Jones", "hairColor":"Brown"}
