function mask (params) {
    // MASK
    let arrays = []

    params.forEach(param => {
        let newArray = JSON.parse(param).sort((a, b) => b - a);
        let present = arrays.find(a => JSON.stringify(a) == JSON.stringify(newArray));
        (!present) ? arrays.push(newArray) : 'pass';
    });

    arrays.sort((a, b) => a.length - b.length);

    arrays.forEach(arr => { console.log(`[${arr.join(', ')}]`); });
}

mask(["[-3, -2, -1, 0, 1, 2, 3, 4]",
"[10, 1, -17, 0, 2, 13]",
"[4, -3, 3, -2, 2, -1, 1, 0]"]);
// [13, 10, 2, 1, 0, -17]
// [4, 3, 2, 1, 0, -1, -2, -3]

console.log('-------------------------------------');

mask(["[7.14, 7.180, 7.339, 80.099]",
"[7.339, 80.0990, 7.140000, 7.18]",
"[7.339, 7.180, 7.14, 80.099]"]);
// [80.099, 7.339, 7.18, 7.14]
