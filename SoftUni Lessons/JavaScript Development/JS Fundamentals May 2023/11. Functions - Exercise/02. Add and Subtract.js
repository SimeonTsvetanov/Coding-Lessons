function addAndSubtract(a, b, c) {
    function add(a, b) {
        return a + b;
    }

    function subtract(result, c) {
        return result - c;
    }

    console.log(subtract(add(a, b), c));
}


addAndSubtract(23, 6, 10);  // 19