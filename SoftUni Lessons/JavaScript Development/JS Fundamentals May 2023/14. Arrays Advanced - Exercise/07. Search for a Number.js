function mask (...params) {
    // MASK
    // You will receive two arrays of integers. The second array is containing exactly three numbers.
    let integers = params[0].map(Number);
    let other = params[1].map(Number);

    // The first number represents the number of elements you have to take from the first array
    // (starting from the first one)
    // The second number represents the number of elements you have to delete from the numbers you took (starting
    // from the first one)
    let result = integers.slice(0, other[0]).splice(other[1]);

    // The third number is the number we search in our collection after the manipulations.
    let searchedNumber = other[2];

    // As output print how many times that number occurs in our array in the following format:
    console.log(`Number ${searchedNumber} occurs ${result.filter(x => x === searchedNumber).length} times.`);
}

mask([5, 2, 3, 4, 1, 6],
[5, 2, 3]);
// Number 3 occurs 1
// times.

console.log('-------------------------------------');

mask([7, 1, 5, 8, 2, 7],
[3, 1, 5]);
// Number 5 occurs 1
// times.
