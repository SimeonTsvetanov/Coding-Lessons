function mask (...params) {
    // MASK
    let [a, b] = params;
    a.forEach(element => {
        b.includes(element) ? console.log(element) : 'pass';
    });
}

mask(['Hey', 'hello', 2, 4, 'Peter', 'e'],
['Petar', 10, 'hey', 4, 'hello', '2']);
// hello
// 4

mask(['S', 'o', 'f', 't', 'U', 'n', 'i', ' '],
['s', 'o', 'c', 'i', 'a', 'l']);
// o
// i
