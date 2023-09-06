function mask (...params) {
    // MASK
    let [array, rotations] = params;

    for(let i = 1; i <= rotations; i++) {
        array.push(array.shift());
    }

    console.log(...array)
}

mask([51, 47, 32, 61, 21], 2);
// 32 61 21 51 47

mask([32, 21, 61, 1], 4);
// 32 21 61 1
