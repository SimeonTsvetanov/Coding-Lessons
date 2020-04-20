function commonElements(first, second) {
    // Mask
    for (let element of first) {
        if (second.includes(element)) {
            console.log(element);
        }
    }
}

commonElements(['Hey', 'hello', 2, 4, 'Peter', 'e'], ['Petar', 10, 'hey', 4, 'hello', '2']);
// Should return:
// hello
// 4

commonElements(['S', 'o', 'f', 't', 'U', 'n', 'i', ' '], ['s', 'o', 'c', 'i', 'a', 'l']);
// Should return:
// o
// i
