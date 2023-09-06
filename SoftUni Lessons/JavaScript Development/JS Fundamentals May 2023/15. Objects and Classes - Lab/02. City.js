function mask (object) {
    // MASK
    for (const [key, value] of Object.entries(object)) {
        console.log(`${key} -> ${value}`);
    }
}

mask({
    name: "Sofia",
    area: 492,
    population: 1238438,
    country: "Bulgaria",
    postCode: "1000"
});
// name -> Sofia
// area -> 492
// population -> 1238438
// country -> Bulgaria
// postCode -> 1000

console.log('-------------------------------------');

mask({
 name: "Plovdiv",
 area: 389,
 population: 1162358,
 country: "Bulgaria",
 postCode: "4000"
}
);
// name -> Plovdiv
// area -> 389
// population -> 1162358
// country -> Bulgaria
// postCode -> 4000
