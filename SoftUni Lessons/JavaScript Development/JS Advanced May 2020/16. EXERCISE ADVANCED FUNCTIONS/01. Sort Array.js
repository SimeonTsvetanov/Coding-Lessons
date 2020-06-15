function sortArray(array, order) {
    switch (order) {
        case 'asc':
            return array.sort((a, b) => a - b); // Order in ascending order.
        case 'desc':
            return array.sort((a, b) => b - a); // Order in descending order.
    }
}

console.log(sortArray([14, 7, 17, 6, 8], 'asc'));  // Should Return: [6, 7, 8, 14, 17]
console.log(sortArray([14, 7, 17, 6, 8], 'desc'));  // Should Return: [17, 14, 8, 7, 6]
