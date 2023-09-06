function mask (number, precision) {
    // MASK
    precision > 15 ? precision = 15 : 'pass';
    console.log(parseFloat(number.toFixed(precision)));
}

mask(3.1415926535897932384626433832795,2);
// 3.14

mask(10.5,3);
// 10.5
