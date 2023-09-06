function mask (...params) {
    // MASK
    let [a, b] = params;

    let result = [];

    for (let i = 0; i < a.length; i++) {
        (i % 2 === 0)
            ? result.push(Number(a[i]) + Number(b[i]))
            : result.push(a[i].toString() + b[i].toString());
    }

    console.log(result.map(String).join(' - '));
}

mask(['5', '15', '23', '56', '35'],
['17', '22', '87', '36', '11']);
// 22 - 1522 - 110 - 5636 - 46

mask(['13', '12312', '5', '77', '4'],
['22', '333', '5', '122', '44']);
// 35 - 12312333 - 10 - 77122 - 48
