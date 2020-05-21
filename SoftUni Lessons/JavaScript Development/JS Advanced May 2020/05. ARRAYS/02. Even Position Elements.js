function evenPositionElement(array = []) {
    // Mask
    let evens = [];
    for (let [index, item] of array.entries()) {
        index % 2 === 0 ? evens.push(item) : 'pass';
    }
    console.log(evens.join(' '));
}

evenPositionElement(['20', '30', '40']);  // Should return: 20 40

evenPositionElement(['5', '10']);  // Should return: 5
