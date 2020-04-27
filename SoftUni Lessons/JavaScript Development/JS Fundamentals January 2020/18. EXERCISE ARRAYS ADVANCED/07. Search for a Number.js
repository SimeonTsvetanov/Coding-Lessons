function searchForANumber(array, data) {
    // Mask
    let [takeCount, deleteCount, searchedNumber] = data;  // Get them Numbers
    array.splice(takeCount);  // Take only the needed
    array.splice(0, deleteCount);  // Remove the first n numbers
    let count = array.filter(x => x === searchedNumber).length;  // Count the occurrences of the searched number.
    console.log(`Number ${searchedNumber} occurs ${count} times.`);  // Log the Result.
}

searchForANumber([5, 2, 3, 4, 1, 6], [5, 2, 3]);
// Should return: "Number 3 occurs 1 times."
