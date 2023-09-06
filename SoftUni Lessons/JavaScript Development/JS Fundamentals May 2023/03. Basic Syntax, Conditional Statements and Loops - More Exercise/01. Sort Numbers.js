function mask (...params) {
    // MASK
    for (let i of params.sort((a, b) => b - a)) {
        console.log(i)
    }
}

mask(2, 1, 3);
//

mask(-2, 1, 3);
//
