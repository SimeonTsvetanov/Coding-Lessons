function convertToObject(json) {
    // Mask
    let person = JSON.parse(json);

    for (let [key, value] of Object.entries(person)) {
        console.log(`${key}: ${value}`);
    }
}

convertToObject('{"name": "George", "age": 40, "town": "Sofia"}');  // Should return:
// name: George
// age: 40
// town: Sofia

convertToObject('{"name": "Simeon", "age": 30, "town": "Smolyan"}');  // Should return:
// name: Simeon
// age: 30
// town: Smolyan
