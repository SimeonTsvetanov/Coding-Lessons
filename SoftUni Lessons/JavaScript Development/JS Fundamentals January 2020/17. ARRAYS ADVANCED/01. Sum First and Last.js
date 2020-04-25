function sumFirstLast(array) {
    // Mask

    function methodPeek(array) {
        // Method One: Gentle
        array = array.map(Number);
        console.log(array[0] + array[array.length - 1]);
    }

    function methodRemove(array) {
        // Method Two: Rape
        let first = Number(array.shift());
        let last = Number(array.pop());
        console.log(first + last);
    }

    methodPeek(array);
    // methodRemove(array);
}

sumFirstLast(['20', '30', '40']);  // Should return: 60

sumFirstLast(['5', '10']);  // Should return: 15