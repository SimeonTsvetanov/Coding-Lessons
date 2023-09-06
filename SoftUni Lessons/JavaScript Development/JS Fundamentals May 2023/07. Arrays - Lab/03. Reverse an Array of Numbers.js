function mask (...params) {
    // MASK
    let [n, elements] = params;

    let result = elements.slice(0, n).reverse().join(' ');

    console.log(result)
}

mask(3, [10, 20, 30, 40, 50] );
// 30 20 10

mask(4, [-1, 20, 99, 5] );
// 5 99 20 -1
