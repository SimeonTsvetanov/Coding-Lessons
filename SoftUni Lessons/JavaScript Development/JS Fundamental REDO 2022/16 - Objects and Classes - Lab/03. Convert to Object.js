function convertToObject (json) {
    // MasK

    let person = JSON.parse(json);

    Object.entries(person).forEach(([key, value]) => {
        console.log(`${key}: ${value}`);
    });
}

convertToObject('{"name": "George", "age": 40, "town": "Sofia"}');
// name: George
// age: 40
// town: Sofia
