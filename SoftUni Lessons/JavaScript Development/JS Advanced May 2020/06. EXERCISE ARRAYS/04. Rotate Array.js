function rotateArray(array = []) {
    // Mask: Optimisation was required...
    let times = Number(array.pop()) % array.length;

    for (let time = 1; time <= times; time++) {
        array.unshift(array.pop());
    }

    console.log(array.join(' '));
}

rotateArray(['1', '2', '3', '4', '2']);  // Should return: 3 4 1 2

rotateArray(['Banana', 'Orange', 'Coconut', 'Apple', '15']);
// Should return: Orange Coconut Apple Banana