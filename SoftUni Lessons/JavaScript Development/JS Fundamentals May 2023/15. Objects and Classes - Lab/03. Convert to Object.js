function mask (params) {
    // MASK
    const object = JSON.parse(params);
    for (const [key, value] of Object.entries(object)) {
        console.log(`${key}: ${value}`);
    }
}

mask('{"name": "George", "age": 40, "town": "Sofia"}');
// name: George
// age: 40
// town: Sofia

console.log('-------------------------------------');

mask('{"name": "Peter", "age": 35, "town": "Plovdiv"}');
// name: Peter
// age: 35
// town: Plovdiv
